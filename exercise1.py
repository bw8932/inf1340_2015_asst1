#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

#test to see if pycharm is configured to push to github
#first calculate the purchase details
shares_bought = 2000
price_bought = 900
share_expense = price_bought * shares_bought
commission_bought = .3 * share_expense
total_expense = share_expense + commission_bought

print (share_expense)
print (total_expense)


#calculate the sale detailss
shares_sold = 2000
price_sold = 942.75
sale_income = shares_sold * price_sold
commission_sold = .3 * sale_income
total_sale_income = sale_income - commission_sold

print (sale_income)
print (total_sale_income)


#calculate the net
money = total_sale_income - total_expense
print ("Lakshmi's investing netted her $%s") % (money)


#initial copy had these lines... that's why I called her overall outcome variable "money"
#does this mean we're to subtract that final net from a $1000 initial amount???
    #money = 1000.00
    #print(money)