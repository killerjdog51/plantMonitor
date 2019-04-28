from Sensors.sensor import soilSensor
from PlantAlmanac.succulent import aloeVera
import time
import datetime
Soil = soilSensor('a:0:o')
Plant = aloeVera()

Plant.displayInfo()
while True:
    Soil.displayPercentage
    Soil.displayValueType
    Plant.checkWater(Soil.getSensorValue)
    time.sleep(1)
