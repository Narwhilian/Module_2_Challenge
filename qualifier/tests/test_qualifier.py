# Import pathlib
from app import find_qualifying_loans
from pathlib import Path
import pathlib

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

    # We establish the output path disired on the test specifications
    # we also use our original data sheet daily_rate_sheet.csv as our comparison data to write in the test

    path_out = Path('./data/output/qualifying_loans.csv')
    path_in = Path('./data/daily_rate_sheet.csv')


    # in there we load our original data sheet and then run it through the save_csv function on our specified path out
    # this should save an identical CSV (minus header changes) to the new file location
    test_results = fileio.load_csv(path_in)
    fileio.save_csv(test_results, path_out)

    # finally we use our load_csv function again on both the newly saved file and the original
    # since no filters were run through it the data should be unchanged
    # thus proving the save_csv function was succesful saving a copy of the previous file in a new location
    assert fileio.load_csv(path_out) == fileio.load_csv(path_in)


def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!

    correct_results = fileio.load_csv(Path('./data/test_data/correct_results_for_filter_test.csv'))
    
    assert find_qualifying_loans(bank_data, current_credit_score, debt, income, loan, home_value) == correct_results
