class Campus:
    def __init__(self, buildings, num_buildings, capacity):
        self.buildings = buildings
        self.num_buildings = num_buildings
        self.capacity = capacity

    def get_info(self):
        print("The campus had {} building(s) with a combined capacity of {} people".format(self.num_buildings, self.capacity))

    def add_building(self, b_object):
        self.buildings.append(b_object.name)
        self.num_buildings += 1
        self.capacity += b_object.capacity
