#!usr/bin/env python3


class Figure:
    def __init__(self, name, width, length):
        self.name = name
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


first_figure = Figure("First cube", 5, 6)
second_figure = Figure("Second cube", 7, 8)

print("{} length == {} length = {}".format(first_figure.name, second_figure.name,
                                           first_figure.length == second_figure.length))
print("{} width == {} width = {}".format(first_figure.name, second_figure.name,
                                         first_figure.width == second_figure.width))
print("")

print("{} length < {} length = {}".format(first_figure.name, second_figure.name,
                                          first_figure.length < second_figure.length))
print("{} width < {} width = {}".format(first_figure.name, second_figure.name,
                                        first_figure.width < second_figure.width))
print("")

print("{} length > {} length = {}".format(first_figure.name, second_figure.name,
                                          first_figure.length > second_figure.length))
print("{} width > {} width = {}".format(first_figure.name, second_figure.name,
                                        first_figure.width > second_figure.width))
print("")

print("{} length <= {} length = {}".format(first_figure.name, second_figure.name,
                                           first_figure.length <= second_figure.length))
print("{} width <= {} width = {}".format(first_figure.name, second_figure.name,
                                         first_figure.width <= second_figure.width))
print("")

print("{} length >= {} length = {}".format(first_figure.name, second_figure.name,
                                           first_figure.length >= second_figure.length))
print("{} width >= {} width = {}".format(first_figure.name, second_figure.name,
                                         first_figure.width >= second_figure.width))
print("")

print("{} length != {} length = {}".format(first_figure.name, second_figure.name,
                                           first_figure.length != second_figure.length))
print("{} width != {} width = {}".format(first_figure.name, second_figure.name,
                                         first_figure.width != second_figure.width))
