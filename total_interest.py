import json
import sys

def get_interest_amount(i):
    loan_amount = i['LoanAmount']
    period = i['PeriodInMonths']
    interest = i['InterestRateIn%']
    final_interest = interest/100/12

    monthly_payment = loan_amount * (final_interest * (1+final_interest) ** period) / ((1+final_interest)** period - 1)

    total_interest = (monthly_payment*period) - loan_amount

    return total_interest

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: total_interest.py filename.json')
    else:
        file = sys.argv[1]
        f = open(file)
        data = json.load(f)
        for i in data['Loans']:
            print(get_interest_amount(i))