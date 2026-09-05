# Q-GlaRe+


## About Q-GlaRe+
Q-GlaRe+ is an open-source QGIS plugin for flowline-based palaeoglacier reconstruction and equilibrium-line altitude (ELA) estimation using geomorphological and topographic data. Q-GlaRe+ is built on tools such as GlaRe (Pellitero et al., 2015, 2016) and PalaeoIce (Li, 2023), which provide open-source code, but require proprietary GIS software licences which may create prohibitive barriers for researchers and institutions. Q-GlaRe+ implements similar algorithms within QGIS, ensuring that software licensing requirements do not determine access to glacier reconstruction capabilities. Validation demonstrates that Q-GlaRe+ maintains scientific accuracy whilst removing these platform dependencies.

The plugin adds a **Q-GlaRe+** provider to the QGIS **Processing Toolbox** with five tools.

## Requirements

- **QGIS 3.20 or later**, with NumPy and Pandas (both bundled with standard QGIS / OSGeo4W installations).
- **SAGA GIS** and the **Processing Saga NextGen Provider** QGIS plugin — required by the
  **3D Interpolation** tool, which calls SAGA's Thin Plate Spline TIN algorithm. The other
  four tools run without SAGA.

### Installing SAGA (for the 3D Interpolation tool)

1. Install SAGA GIS from [saga-gis.org](https://saga-gis.org/) - on Windows extract it to a
   known folder (e.g. `C:\saga-gis`); on macOS `brew install saga-gis`; on Linux use your
   package manager (e.g. `sudo apt install saga`).
2. In QGIS, go to **Settings --> Options --> Processing --> Providers --> SAGA** and set the SAGA
   folder to the directory containing `saga_cmd`.
3. Install the **Processing Saga NextGen Provider** plugin: **Plugins --> Manage and Install
   Plugins**, search for it, and click Install.

## Installation

Q-GlaRe+ is installed from a ZIP file. It is not yet in the official QGIS Plugin Repository,
so it will not appear if you search the Plugin Manager.

1. Download the latest release ZIP from the [Releases page](https://github.com/bsburnham/Q-GlaRe/releases).
2. In QGIS, go to **Plugins --> Manage and Install Plugins --> Install from ZIP**, select the
   downloaded ZIP, and click **Install Plugin**.

Once installed, the tools appear under **Processing → Toolbox → Q-GlaRe+**.

## Tools

| # | Tool | Purpose |
|---|------|---------|
| 1 | 2D FL Ice Thickness | Estimate ice thickness and surface elevation along flowlines |
| 2 | 2D modified FL Ice Thickness | Adjust selected point values and re-run the reconstruction |
| 3 | 2D shape-factor FL Ice Thickness | Apply a valley shape-factor (F-factor) correction using transects |
| 4 | 3D Interpolation | Reconstruct a full 3D glacier surface + thickness raster (uses SAGA TPS) |
| 5 | Q-ELA | Calculate the Equilibrium Line Altitude |

## Input data

All input layers must share the same **projected** CRS (e.g. UTM). Geographic (lat/lon) CRS is
rejected, and the plugin raises a clear error if layers disagree.

- **DEM** - a GDAL-readable raster (GeoTIFF recommended) covering the full glacier extent, in a
  projected CRS.
- **Flowlines** - vector line features digitised along the glacier centreline, from the
  **terminus (lowest elevation)** to the **headwall (highest)**. Tributaries are supported as
  separate features. Lines digitised in reverse are auto-detected against the bed elevation and
  corrected, with a warning.
- **Basin polygon** - a polygon of the palaeo/extant glacier extent, required by **3D Interpolation**.
- **Valley transects** - line features drawn perpendicular to flow, spanning the valley width;
  required only by **2D shape-factor FL Ice Thickness**.

## Workflow

Run the tools in sequence (steps 2 and 3 are optional):

1. **2D FL Ice Thickness** - samples the DEM along each flowline and applies the laminar-flow
   equation, `h = τ_b / (ρ · g · sin α)`, to estimate ice thickness at each point (`h` =
   thickness, `τ_b` = basal shear stress, `ρ` = ice density ~910 kg m⁻³, `g` = 9.81 m s⁻², `α`
   = surface slope). **Output:** a point layer with `ice_thickness`, `ice_surface`, and DEM
   elevation.
2. *(optional)* **2D modified FL Ice Thickness** - select points and adjust their values (e.g.
   basal shear stress) to honour geomorphological constraints such as moraines or trimlines,
   then re-run.
3. *(optional)* **2D shape-factor FL Ice Thickness** - apply an F-factor correction for lateral
   drag using valley transects; important for narrow, deep valleys where the laminar-flow
   equation overestimates thickness.
4. **3D Interpolation** - interpolates the flowline points into a continuous **glacier surface
   raster** and **ice-thickness raster** using SAGA's Thin Plate Spline. Requires the DEM and
   the basin polygon.
5. **Q-ELA** - computes the ELA from a glacier surface raster by **AABR** (default balance
   ratio 1.56), **AAR** (default 0.58), or **AA**. **Output:** ELA contour line(s).

Each run writes a diagnostic log to `qglare_plus_logs/` beside your QGIS project file; check it
if a tool reports an error.

## Licence

Q-GlaRe+ is free software released under the
[GNU General Public Licence v3.0](https://www.gnu.org/licenses/gpl-3.0.html) or later. See
[`LICENSE`](LICENSE).


#### Plugin Test (in QGIS)

To verify the plugin imported correctly:

1. Open QGIS.
2. Go to `Plugins` > `Python Console`.
3. Open an `External Editor` session 
4. Open/import the `qglare_install_test.py` script.
5. Execute to check if plugin was succcessfully installed into QGIS session.

## Citing Q-GlaRe+
This software is published in Earth Surface Processes and Landforms. 

Burnham, B. S., M. Spagnolo, R. Pellitero, et al. 2026. “ Q-GlaRe+: An Open-Source Framework for Palaeoglacier Reconstruction and Equilibrium-Line Altitude Calculation.” Earth Surface Processes and Landforms 51, no. 9: e70406. https://doi.org/10.1002/esp.70406.

