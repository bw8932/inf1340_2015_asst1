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
    print("We're so sorry your car isn't working. Help us diagnose the issue - "\
          "please respond with 'y' for Yes and 'n' for No.")

    print("The battery cables may be damaged. Replace cables and try again.")


diagnose_car()

#first I want to convert standard answers into Boolean operators
query=str(raw_input("Yes or No? "))
#uncertain why this works with just one entry but not when adding additional entry of "yes" and "no" fixed
if query==str("y") or query==str("yes"):
    answer=1
elif query==str("n") or query==str("no"):
    answer=0
else:
    answer=str("Cannot recognize your answer.")

print (answer)
#Does not refer back to my boolean conversion above. Perhaps this functionality is possible with loops.
#I suspect for this exercise converting multiple inputs into boolean operators is overcomplicating to no real purpose.
query=str(raw_input("Now yes or No? "))

print bool(answer)


