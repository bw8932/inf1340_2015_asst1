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

    Inputs: (y,y)

    Expected Outputs: (battery terminals

    Errors:

    """

    # I threw in some spaces to open it up a bit
    # Looks great, man.

    # Clarify required inputs for the program
    print("We're so sorry your car isn't working. Help us diagnose the issue - "
          "please respond with 'y' for Yes and 'n' for No.")

    # Begin nested if statements
    silent = str(raw_input("Is the car silent when you turn the key? "))

    if silent == "y":
        corroded = str(raw_input("Are the battery terminals corroded? "))

        if corroded == "y":
            print("The battery terminals may not be conductive. Clean terminals and try starting again.")

        elif corroded == "n":
            print("The battery cables may be damaged. Replace cables and try again.")

        # Incorrect entry to restart sequence from the beginning
        else:
            print("Improper command. Please try again. \n")
            diagnose_car()

    elif silent == "n":
        clicking = str(raw_input("Does the car make a clicking noise? "))

        if clicking == "y":
            print("The battery is dead. Replace the battery.")

        elif clicking == "n":
            crank = str(raw_input("Does the car crank up but fail to start? "))

            if crank == "y":
                print("The spark plug may be loose. Check spark plug connections.")

            elif crank == "n":
                start_die = str(raw_input("Does the engine start then die? "))

                if start_die == "y":
                    fuel = str(raw_input("Does your car have fuel injection? "))

                    if fuel == "y":
                        print("This issue requires a mechanic. Get it in for service.")

                    elif fuel == "n":
                        print("The choke may be stuck. Check to ensure choke is opening and closing.")

                    else:
                        print("Improper command. Please try again. \n")
                        diagnose_car()

                elif start_die == "n":
                    print("Engine is not getting enough fuel. Clean fuel pump.")

                else:
                    print("Improper command. Please try again. \n")
                    diagnose_car()

            else:
                print("Improper command. Please try again. \n")
                diagnose_car()

        else:
            print("Improper command. Please try again. \n")
            diagnose_car()

    else:
            print("Improper command. Please try again. \n")
            diagnose_car()

diagnose_car()


