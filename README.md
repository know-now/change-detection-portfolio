🏗️ Automated Change Detection on Construction Sites
====================================================

This is a portfolio project designed to demonstrate skills in **geomatics** and **image processing**, specifically tailored to the requirements of the _"Ingénieur(e) - Géomatique & IA"_ position.

The goal of this project is to **automatically detect and visualize changes** on a construction site by comparing two orthophotos taken at different times. This task directly addresses the job description's requirements to:

*   _apply artificial intelligence for change detection (détection de changements)_
    
*   _automate workflows_
    

📋 Key Features
---------------

*   **Image Comparison**: The script takes two geospatial raster files (.tif) as input.
    
*   **Change Detection**: Uses pixel-by-pixel comparison to identify areas with significant differences.
    
*   **Result Vectorization**: Creates a vector file (.geojson) outlining the zones of change for further analysis in GIS software (QGIS, ArcGIS).
    
*   **Visualization**: Generates a raster mask image that clearly highlights the detected changes.
    

🛠️ Tech Stack
--------------

*   **Language**: Python 3.9+
    
*   **Core Libraries**:
    
    *   rasterio – For reading and writing geospatial raster data
        
    *   geopandas – For handling vector data and saving results to GeoJSON
        
    *   scikit-image – For image processing algorithms
        
    *   numpy – For numerical operations with arrays
        

🚀 How to Run the Project
-------------------------

### Step 1: Clone the Repository

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/your-username/change-detection-portfolio.git  cd change-detection-portfolio   `

### Step 2: Create a Virtual Environment and Install Dependencies

It is recommended to use a virtual environment to avoid library conflicts.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv venv  source venv/bin/activate  # On Windows: venv\Scripts\activate  pip install -r requirements.txt   `

### Step 3: Prepare the Data

*   Obtain two orthophotos of the same area taken at different times in **GeoTIFF (.tif)** format.
    
*   Ensure both images share the same CRS (Coordinate Reference System).
    
*   Place them into the data/ directory.
    
*   Rename the files:
    
    *   before.tif (older image)
        
    *   after.tif (newer image)
        

💡 _Tip: If you don't have your own data, check open datasets like_ [_SEN12-CC_](https://mediatum.ub.tum.de/1474000) _or other aerial imagery sources._

### Step 4: Run the Script

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python src/change_detection.py   `

### Step 5: Check the Results

After execution, two new files will appear in the output/ directory:

*   changes\_mask.tif – Raster image where areas of change are marked in white
    
*   changes\_polygons.geojson – Vector file containing polygons outlining these areas
    

You can open these files in any GIS software (e.g., **QGIS**, **ArcGIS**) to analyze the results.

🎯 How This Project Addresses the Needs of SECO Luxembourg
----------------------------------------------------------

This tool demonstrates the ability to:

*   **Automate** the analysis of geospatial data, reducing manual monitoring time
    
*   **Apply computer vision** to solve practical engineering challenges
    
*   **Structure and analyze large datasets**, turning them into actionable insights
    
*   **Create foundations** for advanced systems such as monitoring platforms and digital twins
