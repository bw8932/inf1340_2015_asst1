#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:  1, 5, 10, 15, J

    Expected Outputs:  Error, Pentagon, Decagon, Error,

    Actual Outputs: Error, Pentagon, Decagon, Error, invalid literal

    Errors: None, unless user inputs letter instead of number, when it returns "invalid literal"

    """
    # user inputs polygon's sides
    sides = int(raw_input("How many sides does the polygon have?"))

    # program prints name of shape
    if sides == 3:
        print ("Triangle")

    elif sides == 4:
        print ("Quadrangle")

    elif sides == 5:
        print ("Pentagon")

    elif sides == 6:
        print ("Hexagon")

    elif sides == 7:
        print ("Heptagon")

    elif sides == 8:
        print ("Octagon")

    elif sides == 9:
        print ("Nonagon")

    elif sides == 10:
        print ("Decagon")

    else:
        print ("Error")
        name_that_shape()


name_that_shape()