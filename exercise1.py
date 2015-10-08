#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Test Cases
# inputs: none
# expected outputs (compared to calculations with pen and paper):
# actual outputs:

def lakshmi():

    # first calculate the purchase details
    shares_bought = 2000
    price_bought = 900
    share_expense = price_bought * shares_bought
    commission_bought = .03 * share_expense
    total_expense = share_expense + commission_bought

    # calculate the sale details
    shares_sold = 2000
    price_sold = 942.75
    sale_income = shares_sold * price_sold
    commission_sold = .03 * sale_income
    total_sale_income = sale_income - commission_sold

    # calculate the net and print it
    money = total_sale_income - total_expense
    print "Lakshmi's investing netted her $%s" % money

lakshmi()

