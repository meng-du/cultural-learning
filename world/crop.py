import random

GROWTH_RATE = 1
RIPE = 10  # harvest at this amount of growth will result in max production, water is not needed after this growth
PRODUCTION_RANDOMNESS = random.gauss(0, 1)  # random number under normal distribution, mu = 0, sigma = 2

class Crop(object):
    def __init__(self, water_constant, initial_water = 0):
        self.WATER_CONST = water_constant  # defines how hard (how much water is needed) to grow this crop
        self.growth = 0
        self.water_needed = self.WATER_CONST - initial_water

    def water(self, amount):
        self.water_needed -= amount
        if self.water_needed <= 0:
            self.water_needed = 0

    def grow(self):
        self.growth += GROWTH_RATE
        if self.growth < RIPE:
            self.water_needed = self.WATER_CONST

    def harvest(self):
        production = (RIPE - abs(self.growth - RIPE)) + PRODUCTION_RANDOMNESS
        if production < 0:
            production = 0
        self.__init__(self.WATER_CONST * 2)
        return production

