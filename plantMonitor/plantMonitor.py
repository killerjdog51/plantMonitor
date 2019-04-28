from Sensors.sensor import soilSensor
import time
Soil = soilSensor('a:0:o')

while True:
    Soil.displayValueType
    Soil.displayPercentage
    
    time.sleep(1)