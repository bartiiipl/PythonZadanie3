#!usr/bin/env python3


class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

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


class MonsterWithArmor(Monster):
    def __init__(self, name, hp, armor):
        self.name = name
        self.hp = hp
        self.armor = armor


class Tank(MonsterWithArmor):
    def __init__(self, name, hp, armor):
        self.name = name
        self.hp = hp
        self.armor = armor


class Wizard(Monster):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Ranger(Monster):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Shielder(MonsterWithArmor):
    def __init__(self, name, hp, armor):
        self.name = name
        self.hp = hp
        self.armor = armor


shielder = Shielder("Shielder", 12, 10)
shielder_other = Shielder("Shielder other", 11, 10)

ranger = Ranger("Ranger", 7)
ranger_other = Ranger("Other ranger", 9)

print("{}".format(shielder.armor == shielder_other.armor))

print("{}".format(ranger.hp == ranger_other.hp))

print("{}".format(ranger.hp == shielder.hp))
