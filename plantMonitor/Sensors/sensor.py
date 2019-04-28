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

    @property
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
        moistureLevel = int(round(self.getSensorValue*1000))
        if(moistureLevel < 1000 and moistureLevel > 750):
            print("Too much Water!!")
        elif(moistureLevel < 750 and moistureLevel > 300):
            print("Soil is moist")
        elif(moistureLevel < 300 and moistureLevel > 0):
            print("Soil is dry")
        else:
            print("Soil is too dry!!")

class sunlightSensor(sensorBase):
    """Sensor Class for monitoring the ambient sunlight"""

    def __init__(self, pin):
        super().__init__(pin)

    @property
    def calculateLuxValue(self):
        logLux = float((int(self.getSensorValue) * 1024 / 5.0))
        return pow(10, logLux)

    @property
    def displayLuxValue(self):
        print(self.calculateLuxValue)

    @property
    def displayLuxType(self):
        luxLevel = self.calculateLuxValue
        if(luxLevel < 0.001):
            print("Cloudy Night")
        elif(luxLevel >= 0.001 and luxLevel < 0.02):
            print("Starlight Night")
        elif(luxLevel >= 0.02 and luxLevel < 1):
            print("Moonlight Night")
        elif(luxLevel >= 1 and luxLevel < 10):
            print("Twilight")
        elif(luxLevel >= 50 and luxLevel < 100):
            print("House Lighting")
        elif(luxLevel >= 100 and luxLevel < 250):
            print("Very Cloudy")
        elif(luxLevel >= 250 and luxLevel < 500):
            print("Sunrise/Sunset")
        elif(luxLevel >= 1000 and luxLevel < 2000):
            print("Cloudy")
        elif(luxLevel >= 2000 and luxLevel < 10000):
            print("Partly Cloudy")
        elif(luxLevel >=10000 and luxLevel < 25000):
            print("Partial Sunlight (shade)")
        elif(luxLevel >= 25000 and luxLevel < 32000):
            print("Full Sunlight")
        elif(luxLevel >= 32000 and luxLevel < 130000):
            print("Direct Sunlight")