import crop

INITIAL_FOOD = 5  # an agent needs food to be alive
INITIAL_WATER = 5  # used to water the crops
INITIAL_NUM_CROPS = 5
CROP_WATER_CONSTANT = 10


initial_crops = []
for i in range(INITIAL_NUM_CROPS):
    initial_crops.append(crop.Crop(CROP_WATER_CONSTANT))

class Agent(object):
    def __init__(self):
        self.food = INITIAL_FOOD
        self.crops = list(initial_crops)
        self.water = INITIAL_WATER

    # Actions available:
    def act(self):
