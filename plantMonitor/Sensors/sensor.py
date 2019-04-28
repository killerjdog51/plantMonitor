from pyfirmata import Arduino, util

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

class sensorBase(object):
    """Base sensor class used to build other sensors"""

    def __init__(self, pin):
        self._pin = board.get_pin(pin)

    @property
    def getSensorValue(self):
        val = self._pin.read()
        if(val == None):
            val = 0.0
        return val

    def displaySensorValue(self):
        print("{}".format(self.getSensorValue))


class soilSensor(sensorBase):
    """Sensor class for monitoring the soil moisture level"""

    def __init__(self, pin):
        super().__init__(pin)

    @property
    def displayPercentage(self):
        print("{}%".format(round(self.getSensorValue*100, 2)))

    @property
    def displayValueType(self):
        __moistureLevel = int(round(self.getSensorValue*1000))
        if(__moistureLevel < 1000 and __moistureLevel > 750):
            print("Too much Water!!")
        elif(__moistureLevel < 750 and __moistureLevel > 300):
            print("Soil is moist")
        elif(__moistureLevel < 300 and __moistureLevel > 0):
            print("Soil is dry")
        else:
            print("Soil is too dry!!")

class sunlightSensor(sensorBase):
    """Sensor Class for monitoring the ambient sunlight"""

    def __init__(self, pin):
        super().__init__(pin)

    @property
    def calculateLuxValue(self):
        __logLux = float((int(self.getSensorValue) * 1024 / 5.0))
        return pow(10, __logLux)

    @property
    def displayLuxValue(self):
        print(self.calculateLuxValue)

    @property
    def displayLuxType(self):
        __luxLevel = self.calculateLuxValue
        if(__luxLevel < 0.001):
            print("Cloudy Night")
        elif(__luxLevel >= 0.001 and __luxLevel < 0.02):
            print("Starlight Night")
        elif(__luxLevel >= 0.02 and __luxLevel < 1):
            print("Moonlight Night")
        elif(__luxLevel >= 1 and __luxLevel < 10):
            print("Twilight")
        elif(__luxLevel >= 50 and __luxLevel < 100):
            print("House Lighting")
        elif(__luxLevel >= 100 and __luxLevel < 250):
            print("Very Cloudy")
        elif(__luxLevel >= 250 and __luxLevel < 500):
            print("Sunrise/Sunset")
        elif(__luxLevel >= 1000 and __luxLevel < 2000):
            print("Cloudy")
        elif(__luxLevel >= 2000 and __luxLevel < 10000):
            print("Partly Cloudy")
        elif(__luxLevel >=10000 and __luxLevel < 25000):
            print("Partial Sunlight (shade)")
        elif(__luxLevel >= 25000 and __luxLevel < 32000):
            print("Full Sunlight")
        elif(__luxLevel >= 32000 and __luxLevel < 130000):
            print("Direct Sunlight")