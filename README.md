# Test assignment for Programming Technologies

Program to calculate cumulative interest paid on a loan in specified period of time. 

Formulas used:
 
* monthly payment = loan amount * (interest * (1+interest) ** period) / ((1+interest)** period - 1)

* total interest = (monthly payment * period) - loan amount

Can be run in terminal with the following command:

python total_interest.py filename.json

Note: Please note the format of data inside json file.
