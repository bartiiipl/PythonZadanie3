#!usr/bin/env python3


def compare_name():
    user_name = input("Your name: ")
    if user_name == "Bartek":
        print("Hi Bartek !")
    else:
        print("Hello {} !".format(user_name))


compare_name()
