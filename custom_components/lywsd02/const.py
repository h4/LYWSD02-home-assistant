DOMAIN = "lywsd02"
DOMAIN_DATA = "{}_data".format(DOMAIN)
VERSION = "0.0.4"
PLATFORMS = ["sensor"]
REQUIRED_FILES = [
    "const.py",
    "manifest.json",
    "sensor.py",
]
ISSUE_URL = "https://github.com/h4/LYWSD02-home-assistant/issues"
ATTRIBUTION = "Xiaomi Lywsd02 Temperature and Humidity sensor"
STARTUP = """
-------------------------------------------------------------------
{name}
Version: {version}
This is a custom component
If you have any issues with this you need to open an issue here:
{issueurl}
-------------------------------------------------------------------
"""

ICON = "mdi:mdi-thermometer"

CONF_NAME = "name"
CONF_SENSOR = "sensor"
CONF_ENABLED = "enabled"

DEFAULT_NAME = DOMAIN
