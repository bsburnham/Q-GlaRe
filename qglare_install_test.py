# Test to verify that the plugin is successfully imported into a QGIS session.
# Excute in the QGIS Python Console

plugin_name = 'qglare_plus' 

try:
    __import__(plugin_name)
    print(f"Plugin '{plugin_name}' imported successfully.")
except Exception as e:
    print(f"Failed to load plugin '{plugin_name}': {e}")