# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:28:27 2023

@author: FANKA
"""
#%%
"""
Problem 1 - Paying Debt off in a Year
10.0/10.0 points (graded)
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135 
So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

We provide sample test cases below. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.

Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!
"""
def credit_bal(balance, annualInterestRate, monthlyPaymentRate): 
    months = 1;
    previousBalance = balance
    monthlyInterestRate = annualInterestRate/12
    while months <= 12:
        #minMonthlyPayment = monthlyPaymentRate * previousBalance
        #monthlyUnpaidBal = previousBalance - minMonthlyPayment # subtract monthly payment first
        #monthlyUnpaidBal = previousBalance * (1 - monthlyPaymentRate)
        updatedBalance = (previousBalance * (1 - monthlyPaymentRate)) * (1 + monthlyInterestRate) # then calc interest on what you have left
        previousBalance = updatedBalance # make the updated balance (or remaining balance) the new previous balance
        months += 1
    return round(updatedBalance, 2)

balance = 42; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
print("Remaining balance: " + str(credit_bal(balance, annualInterestRate, monthlyPaymentRate)))
#%%
"""
Problem 2 - Paying Debt Off in a Year
15.0/15.0 points (graded)
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
# Paste your code into this box
def paying_debt(balance, annualInterestRate):
    monthlyPayment = 0
    monthlyInterestRate = annualInterestRate /12
    updatedBalance = balance
    month = 0

    while updatedBalance > 0:
        monthlyPayment += 10
        updatedBalance = balance

        for month in range(1,13):
            updatedBalance -= monthlyPayment
            updatedBalance += monthlyInterestRate * updatedBalance
            month += 1
            #print (updatedBalance)
    return monthlyPayment #"Lowest Payment: %g" % monthlyPayment

balance = 3329; annualInterestRate = 0.2   
print ("Lowest Payment: " + str(paying_debt(balance, annualInterestRate)))
#%%
"""
Problem 3 - Using Bisection Search to Make the Program Faster
20.0/20.0 points (graded)
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious answer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run on our servers.
"""
initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0
month = 0


def calculate(month, balance, minPay, monthlyInterestRate):
    while month < 12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance   
    
while abs(balance) >= epsilon:
    balance = initBalance
    month = 0
    balance = calculate(month, balance, minPay, monthlyInterestRate)
    
    if balance > 0:
        low = minPay
    else:
        high = minPay
    minPay = (high + low)/2.0
    
minPay = round(minPay,2)

print('Lowest Payment: ' + str(minPay))
#%%





























