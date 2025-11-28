# Q-GlaRe+

## Basic Usage

### Setup

1. Create and save a QGIS project in a dedicated folder.
2. Ensure all input layers (raster and vector) use the same CRS.

### Installation

1. Download the plugin ZIP.
2. In QGIS:  
   `Plugins` → `Manage and Install Plugins` → `Install from ZIP`.
3. Select the downloaded ZIP and install.

### Executing Tools

- Tools appear in the **Processing Toolbox** under `Q-GlaRe+`.
- Alternatively, scripts can be imported individually into the Toolbox.

For input requirements and outputs of tools, refer to the tool descriptions in QGIS.

#### Plugin Test (in QGIS)

To verify the plugin imported correctly:

1. Open QGIS.
2. Go to `Plugins` > `Python Console`.
3. Open an `External Editor` session 
4. Open/import the `qglare_install_test.py` script.
5. Execute to check if plugin was succcessfully installed into QGIS session.
