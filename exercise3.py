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

    Inputs: (Y,Y) (N,N,N,N) (z) (N,N,N,Y) (Y,N) (N,N,Y) (N,N,N,Y,Y)

    Expected Outputs: (Clean terminals and try starting again.) (Engine is not getting enough fuel. Clean fuel pump.)
    (Improper command. Please try again.) (Does your car have fuel injection?) (Replace cables and try again.)
    (Check spark plug connections.) (Get it in for service.)

    Errors:

    """

    # Begin nested if statements
    silent = str(raw_input("Is the car silent when you turn the key? "))

    if silent == "Y":
        corroded = str(raw_input("Are the battery terminals corroded? "))

        if corroded == "Y":
            print("Clean terminals and try starting again.")

        elif corroded == "N":
            print("Replace cables and try again.")

        # Incorrect entry to restart sequence from the beginning
        else:
            print("Improper command. Please try again. \n")
            diagnose_car()

    elif silent == "N":
        clicking = str(raw_input("Does the car make a clicking noise? "))

        if clicking == "Y":
            print("Replace the battery.")

        elif clicking == "N":
            crank = str(raw_input("Does the car crank up but fail to start? "))

            if crank == "Y":
                print("Check spark plug connections.")

            elif crank == "N":
                start_die = str(raw_input("Does the engine start then die? "))

                if start_die == "Y":
                    fuel = str(raw_input("Does your car have fuel injection? "))

                    if fuel == "Y":
                        print("Get it in for service.")

                    elif fuel == "N":
                        print("Check to ensure the choke is opening and closing.")

                    else:
                        print("Improper command. Please try again. \n")
                        diagnose_car()

                elif start_die == "N":
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