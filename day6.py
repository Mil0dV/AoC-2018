# filename = "input-day6.txt"
filename = "input-day6-test.txt"

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.__dict__)

def read_coordinates(filename):
    coordinates = []
    file = open(filename, "r")
    for line in file:
        coordinate = Coordinate(line.split())
        coordinates.append(coordinate)

print read_coordinates(filename)
