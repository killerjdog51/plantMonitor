import datetime

class succulentBase(object):
    _plantType = "Cactus"
    _Family = "Asphodelaceae"
    _Species = "Just a Plant"
    _soilType = "Soil"
    _avgWaterCycle = None
    _hardyZones = 0
    _outdoorLight = 0
    _indoorLight = 0
    _minTemp = 0
    _maxTemp = 0

    def displayInfo(self):
        print("Family: {}      Species: {}".format(self._Family, self._Species))
        print("Water Requirements: {}      Every {} weeks".format(self._WaterNeeds, self._avgWaterCycle))
        print("Outside Light Requirements: {}   Indoor Light Requirements: {}".format(self._outdoorLight, self._indoorLight))
        print("Soil Requirements: {}        Hardiness Zones: {}".format(self._soilType, self._hardyZones))
        print("Minimum Temperature: {}      Maximum Temperature {}".format(self._minTemp, self._maxTemp))

    def checkWater(self, sensor):
        __today = datetime.datetime.now()
        __moistureLevel = int(round(sensor*1000))
        __newWaterDate = self._lastWater + datetime.timedelta(weeks=self._avgWaterCycle)
        if(datetime.datetime.now() > __newWaterDate and __moistureLevel <= 300):
            print("Water Me Now!")
        if(datetime.datetime.now() > __newWaterDate and __moistureLevel >= 750):
            self._lastWater = datetime.date.today()
            print("Watered plant on {}".format(self._lastWater))

class aloe(succulentBase):
        _Genus = "Aloe"
        _WaterNeeds = "Low"

class aloeVera(aloe):
    _Species = "Aloe Vera"
    _soilType = "Sandy Soil"
    _avgWaterCycle = 4
    _hardyZones = "8-11"
    _outdoorLight = "6-8 Hours of direct sunlight"
    _indoorLight = "16 Hours of indirect/shaded light"
    _minTemp = 55
    _maxTemp = 80

    def __init__(self):
        self._lastWater = datetime.datetime(datetime.datetime.now().year, 1, 1)