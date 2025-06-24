# Q-GlaRe

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

To verify the plugin loads correctly:

1. Open QGIS.
2. Go to `Plugins` > `Python Console`.
3. Run the following script:

```python
exec(open('plugin_test.py').read())
