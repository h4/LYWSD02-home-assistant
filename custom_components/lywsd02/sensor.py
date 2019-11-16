import logging

from homeassistant.helpers.entity import Entity
from .const import ATTRIBUTION, DEFAULT_NAME, DOMAIN_DATA, ICON

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
        hass,
        config,
        async_add_entities,
        discovery_info=None):  # pylint: disable=unused-argument
    """Setup sensor platform."""
    async_add_entities([Lywsd02Sensor(hass, discovery_info)], True)

class Lywsd02Sensor(Entity):
    """lywsd02 Sensor class."""

    def __init__(self, hass, config):
        self.hass = hass
        self.attr = {}
        self._state = None
        self._name = config.get("name", DEFAULT_NAME)

    async def async_update(self):
        """Update the sensor."""
        # Send update "signal" to the component
        data = await self.hass.data[DOMAIN_DATA]["client"].update_data()

        # Get new data (if any)
        updated = self.hass.data[DOMAIN_DATA]["data"]

        # Check the data and update the value.
        self._state = updated

        # Set/update attributes
        self.attr["attribution"] = ATTRIBUTION
        self.attr["temperature"] = updated.get("temperature")
        self.attr["humidity"] = updated.get("humidity")
        self.attr["battery_level"] = updated.get("battery")
        if updated.get("time"):
            self.attr["time"] = updated.get("time").strftime("%H:%M:%S")

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.environmental_index

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.attr

    @property
    def environmental_index(self):
        temp_index = 'Comfort'
        humid_index = 'Comfort'
        t = self._state.get('temperature')
        h = self._state.get('humidity')
        if t < 21:
            temp_index = 'Cold'
        if t > 26:
            temp_index = 'Hot'
        if h < 40:
            humid_index = 'Dry'
        if h > 60:
            humid_index = 'Dump'
        if humid_index != 'Comfort':
            if temp_index != 'Comfort':
                return '{} and {}'.format(temp_index, humid_index)
            else:
                return humid_index
        return temp_index