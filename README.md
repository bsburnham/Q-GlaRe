# Q-GlaRe+

[![DOI](https://zenodo.org/badge/1007573102.svg)](https://doi.org/10.5281/zenodo.15828546)

## About Q-GlaRe+
Q-GlaRe+ is an open-source QGIS plugin for flowline-based palaeoglacier reconstruction and equilibrium-line altitude (ELA) estimation using geomorphological and topographic data. Q-GlaRe+ is built on tools such as GlaRe (Pellitero et al., 2015, 2016) and PalaeoIce (Li, 2023), which provide open-source code, but require proprietary GIS software licences which may create prohibitive barriers for researchers and institutions. Q-GlaRe+ implements similar algorithms within QGIS, ensuring that software licensing requirements do not determine access to glacier reconstruction capabilities. Validation demonstrates that Q-GlaRe+ maintains scientific accuracy whilst removing these platform dependencies.

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

## Citing Q-GlaRe+
This software is currently under peer review for publication; the archived release is available via Zenodo (DOI listed above).

- `Harvard`: Burnham, B.S. (2026) ‘Q-GlaRe+: An open-source framework for palaeoglacier reconstruction and equilibrium-line altitude calculation’. Zenodo. doi:10.5281/zenodo.18631046.
- `APA`: Burnham, B. S., Spagnolo, M., Pellitero, R., Li, Y., Barr, I., Rea, B. R., & Kaselouris, A. (2026). Q-GlaRe+: An open-source framework for palaeoglacier reconstruction and equilibrium-line altitude calculation (0.1.1). Zenodo. https://doi.org/10.5281/zenodo.18631046
