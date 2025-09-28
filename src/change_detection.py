import rasterio
from rasterio.features import shapes
import geopandas as gpd
import numpy as np
from skimage.filters import threshold_otsu
from skimage.morphology import remove_small_objects, remove_small_holes
import os
from shapely.geometry import shape

def detect_changes(before_path, after_path, output_dir):
    """
    Виявляє зміни між двома геопросторовими зображеннями.

    Args:
        before_path (str): Шлях до зображення "до".
        after_path (str): Шлях до зображення "після".
        output_dir (str): Папка для збереження результатів.
    """
    print("Процес розпочато...")

    # Крок 1: Відкриття зображень та читання метаданих
    with rasterio.open(before_path) as before_src, rasterio.open(after_path) as after_src:
        # Перевірка, чи збігаються системи координат та розміри
        if before_src.crs != after_src.crs or before_src.shape != after_src.shape:
            raise ValueError("Зображення мають різні розміри або системи координат. Потрібна попередня обробка.")

        # Читаємо зображення як масиви NumPy
        before_img = before_src.read(1).astype('float32')
        after_img = after_src.read(1).astype('float32')
        
        # Зберігаємо метадані для запису результату
        profile = before_src.profile
        profile.update(dtype=rasterio.uint8, count=1)

    print("Зображення успішно завантажено.")

    # Крок 2: Розрахунок різниці між зображеннями
    # Використовуємо абсолютну різницю, щоб знайти місця змін
    diff_img = np.abs(after_img - before_img)

    # Нормалізуємо різницю до діапазону 0-255 для візуалізації та аналізу
    diff_normalized = ((diff_img - diff_img.min()) / (diff_img.max() - diff_img.min()) * 255).astype(np.uint8)

    # Крок 3: Визначення порогу для виділення значних змін
    # Використовуємо метод Оцу для автоматичного визначення порогу
    thresh = threshold_otsu(diff_normalized)
    binary_mask = diff_normalized > thresh
    
    print(f"Автоматично визначений поріг для змін: {thresh}")

    # Крок 4: Очищення маски від шуму
    # Видаляємо малі об'єкти (шум)
    cleaned_mask = remove_small_objects(binary_mask, min_size=500) # min_size можна налаштувати
    # Заповнюємо невеликі "дірки" в об'єктах
    cleaned_mask = remove_small_holes(cleaned_mask, area_threshold=250)
    
    # Перетворюємо булеву маску в цілочисельний формат (0 або 255)
    final_mask = cleaned_mask.astype(np.uint8) * 255
    
    print("Маска змін створена та очищена від шуму.")

    # Крок 5: Збереження растрової маски змін
    mask_path = os.path.join(output_dir, "changes_mask.tif")
    with rasterio.open(mask_path, 'w', **profile) as dst:
        dst.write(final_mask, 1)
    
    print(f"Растрова маска змін збережена у файл: {mask_path}")

    # Крок 6: Векторизація результатів
    # Перетворюємо растрову маску на векторні полігони
    mask_shapes = shapes(final_mask, mask=(final_mask > 0), transform=before_src.transform)
    
    # Створюємо GeoDataFrame з отриманих полігонів
    geometries = [shape(geom) for geom, value in mask_shapes]
    gdf = gpd.GeoDataFrame(geometry=geometries, crs=before_src.crs)
    
    # Зберігаємо векторний файл
    geojson_path = os.path.join(output_dir, "changes_polygons.geojson")
    gdf.to_file(geojson_path, driver='GeoJSON')
    
    print(f"Векторні полігони змін збережено у файл: {geojson_path}")
    print("Процес успішно завершено!")


if __name__ == '__main__':
    # Визначення шляхів до файлів
    # Скрипт очікує, що він знаходиться в папці src/, а дані - в data/
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

    # Створення папки для результатів, якщо її не існує
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Шляхи до вхідних зображень
    before_image_path = os.path.join(DATA_DIR, 'before.tif')
    after_image_path = os.path.join(DATA_DIR, 'after.tif')
    
    # Перевірка наявності файлів
    if not os.path.exists(before_image_path) or not os.path.exists(after_image_path):
        print("Помилка: Переконайтеся, що файли 'before.tif' та 'after.tif' знаходяться в папці 'data'.")
    else:
        detect_changes(before_image_path, after_image_path, OUTPUT_DIR)