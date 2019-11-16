# LYWSD02-home-assistant
Home-Assistant sensor for [Xiaomi LYWSD02 Hygrometer Thermometer](https://www.banggood.com/Xiaomi-Mijia-BT4_0-Wireless-Smart-Electric-Digital-IndoorOutdoor-Hygrometer-Thermometer-Clock-Tools-Set-p-1447044.html?rmmds=myorder&cur_warehouse=CN).

## !WORK IN PROGRESS!

*TODO:* Add more documentation 

# Installation

1. Copy `custom_components/lywsd02` directory into `custom_components` inside your HA directory (typically, where `configuration.yaml` is placed).
2. Add this block into `configuration.yaml`
    ```yaml
    lywsd02:
      mac: 3A:57:C8:89:70:BE
      sensor:
        - enabled: true
          name: 'My Thermometer'
    ```
    where `mac` property is you'r BT Thermometer mac address. See [mitemp_bt docs](https://www.home-assistant.io/components/mitemp_bt/#configuration)
    for instructions.
3. Update or create sensor templates (**this step will be simplified in future**)
    ```yaml
   sensor:
       - platform: template
        sensors:
            my_temp:
                friendly_name: "Entrance Temperature"
                value_template: "{{ states.sensor.my_thermometer.attributes.temperature }}"
                unit_of_measurement: 'ºC'
            my_humid:
                friendly_name: "Entrance Humidity"
                value_template: "{{ states.sensor.my_thermometer.attributes.humidity }}"
                unit_of_measurement: '%'
    ```
4. Restart Home-Assistant

## Available attributes

| Name | Type | Units | Description |
|------|------|-------|-------------|
| tetemperature | float | °C | Temperature measured value |
| humidity | int | % | Relative Humidity measured value |
| battery_level | int | % | *Experimental* Device battery level. I'm not sure that it gets correct | 


![pixel](https://mc.yandex.ru/watch/53742889)
