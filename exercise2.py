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

    Inputs:  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, J

    Expected Outputs:  Error, Error, Error, triangle, quadrilateral, pentagon, hexagon,
     heptagon, octagon, nonagon, decagon, Error, Error

    Actual Outputs: Error, Error, Error, triangle, quadrilateral, pentagon, hexagon,
     heptagon, octagon, nonagon, decagon, Error, Error

    Errors: Error, Error, Error, triangle, quadrilateral, pentagon, hexagon,
     heptagon, octagon, nonagon, decagon, Error, Error

    """
    # user inputs polygon's sides
    sides = (raw_input("How many sides does the polygon have?"))

    # program prints name of shape
    if sides == "3":
        print ("triangle")

    elif sides == "4":
        print ("quadrilateral")

    elif sides == "5":
        print ("pentagon")

    elif sides == "6":
        print ("hexagon")

    elif sides == "7":
        print ("heptagon")

    elif sides == "8":
        print ("octagon")

    elif sides == "9":
        print ("nonagon")

    elif sides == "10":
        print ("decagon")

    else:
        print ("Error")

#commented out call on function so test program will work
#name_that_shape()
