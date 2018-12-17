#!usr/bin/env python3


zero = 0


def compare_number():
    user_number = input("Your number: ")
    user_number = int(user_number)

    if zero is user_number:
        print("It is zero")
    if zero is not user_number:
        print("Your value: {}".format(user_number))


compare_number()
