#!usr/bin/env python3


class Solid:
    def __init__(self, name, height, width, length):
        self.name = name
        self.height = height
        self.width = width
        self.length = length

    def __eq__(self, other):
        print("Comparision type: {} == {}".format(self.name, other.name))
        return self.side_length == other.side_length

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.side_length < other.side_length

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.side_length > other.side_length

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.side_length <= other.side_length

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.side_length >= other.side_length

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.side_length != other.side_length


first_cube = Solid("First cube", 5, 6, 7)
second_cube = Solid("Second cube", 7, 8, 9)

print("{} height == {} height = {}".format(first_cube.name, second_cube.name, first_cube.height == second_cube.height))
print("{} length == {} length = {}".format(first_cube.name, second_cube.name, first_cube.length == second_cube.length))
print("{} width == {} width = {}".format(first_cube.name, second_cube.name, first_cube.width == second_cube.width))
print("")

print("{} height < {} height = {}".format(first_cube.name, second_cube.name, first_cube.height < second_cube.height))
print("{} length < {} length = {}".format(first_cube.name, second_cube.name, first_cube.length < second_cube.length))
print("{} width < {} width = {}".format(first_cube.name, second_cube.name, first_cube.width < second_cube.width))
print("")

print("{} height > {} height = {}".format(first_cube.name, second_cube.name, first_cube.height > second_cube.height))
print("{} length > {} length = {}".format(first_cube.name, second_cube.name, first_cube.length > second_cube.length))
print("{} width > {} width = {}".format(first_cube.name, second_cube.name, first_cube.width > second_cube.width))
print("")

print("{} height <= {} height = {}".format(first_cube.name, second_cube.name, first_cube.height <= second_cube.height))
print("{} length <= {} length = {}".format(first_cube.name, second_cube.name, first_cube.length <= second_cube.length))
print("{} width <= {} width = {}".format(first_cube.name, second_cube.name, first_cube.width <= second_cube.width))
print("")

print("{} height >= {} height = {}".format(first_cube.name, second_cube.name, first_cube.height >= second_cube.height))
print("{} length >= {} length = {}".format(first_cube.name, second_cube.name, first_cube.length >= second_cube.length))
print("{} width >= {} width = {}".format(first_cube.name, second_cube.name, first_cube.width >= second_cube.width))
print("")

print("{} height != {} height = {}".format(first_cube.name, second_cube.name, first_cube.height != second_cube.height))
print("{} length != {} length = {}".format(first_cube.name, second_cube.name, first_cube.length != second_cube.length))
print("{} width != {} width = {}".format(first_cube.name, second_cube.name, first_cube.width != second_cube.width))
