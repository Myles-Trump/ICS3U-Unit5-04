#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program calculates the volume of a cylinder

import math


def volume_of_cylinder(radius_int, height_int):

    # process
    volume = math.pi * radius_int ** 2 * height_int

    # output
    print("\nYour cylinder's volume is {0:,.10} cm³".format(volume))


def main():
    # this function calls other functions as well as
    #   takes input

    # input
    radius = input("Please input the radius (cm): ")
    height = input("Please input the height (cm): ")

    try:
        radius_int = int(radius)
        height_int = int(height)

    except Exception:
        print("\nYou have entered an invalid input.")

    finally:
        # call fucntions
        volume_of_cylinder(radius_int, height_int)


if __name__ == "__main__":
    main()
