#!/usr/bin/python3
# Author - Delbante Alebachew

for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
