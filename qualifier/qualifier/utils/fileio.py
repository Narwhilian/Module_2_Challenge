# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data



def save_csv(qualifying_loans, output_path):
    """Writes a new CSV file in the data file with the name provided by user input.

    Args:
        qualifying_loans (list): the list of qualifying loans to be written.

    Returns:
        Writes and saves a new CSV file, does not return any new data to the function.

    """

    

    with open (output_path, "w", newline= "") as csvfile:
        csvwriter = csv.writer(csvfile)
        header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
        csvwriter.writerow(header)

        for loan in qualifying_loans:
            csvwriter.writerow(loan)

