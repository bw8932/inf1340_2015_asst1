#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """
    print("We're so sorry your car isn't working. Help us diagnose the issue - "
          "please respond with 'Y' for Yes and 'N' for No.")

    silent = raw_input("Is the car silent when you turn the key?")
    if silent == "Y":

        corroded = raw_input("Are the battery terminals corroded?")
        if corroded == "Y":
            print ("Clean terminals and try starting again.")
        elif corroded == "N":
            print ("Replace cables and try again.")

    elif silent == "N":

        click = raw_input("Does the car make a clicking noise?")
        if click == "Y":
            print ("Replace the battery.")

    else:
        print ("Error")



diagnose_car()

#first I want to convert standard answers into Boolean operators
query=str(raw_input("Yes or No? "))
#uncertain why this works with just one entry but not when adding additional entry of "yes" and "no" fixed
if query == str("y") or query == str("yes"):
    answer=1
elif query == str("n") or query == str("no"):
    answer = 0
else:
    answer = str("Error.")

print (answer)
#Does not refer back to my boolean conversion above. Perhaps this functionality is possible with loops.
#I suspect for this exercise converting multiple inputs into boolean operators is overcomplicating to no real purpose.
    #Brady: I think so.  Let's just go with Y or N for simplicity... that seems to be what she was
    #hinting at with her clarifications posting on blackboard
query=str(raw_input("Now yes or No? "))

print bool(answer)


