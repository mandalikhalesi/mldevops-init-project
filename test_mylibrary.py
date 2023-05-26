# File: test_mylibrary.py
# Pytest filename starts with "test_...."
import logging
import pandas as pd
import pytest

# Logging basic config

logging.basicConfig(
    filename="./results.log",
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)

# Function to test

def import_data(pth):
    '''
    Args:
        pth: (str) to import

    Returns:
        df: (DataFrame) data to pass on
    '''

    d_f = pd.read_csv(pth)
    return d_f


# Fixture - The test function test_import_data() will
# use the return of path() as an argument

@pytest.fixture(scope="module")

def path():
    '''
    Path returns the csv file
    '''
    return "./data/bank_data.csv"


# Test method

def test_import_data(path):
    '''
    Args:
        path: (str) to import

    Returns:
        d_f: (DataFrame) data to pass on

    Raises:
        FileNotFoundError: if file is not found or available.
        AssertionError: if file doesn't have rows & columns.
    '''
    try:
        d_f = pd.read_csv(path)
        logging.info("SUCCESS: There are %s rows in your dataframe.", d_f.shape)
        logging.info("SUCCESS: Your file was successfully read in.")

    except FileNotFoundError as err:
        logging.error("ERROR: File wasn't found")
        raise err

        # Check the d_f shape
    try:
        assert d_f.shape[0] > 0
        assert d_f.shape[1] > 0

    except AssertionError as err:
        logging.error(
            "ERROR: Testing import_data: The file doesn't have rows and columns")
        raise err
    return d_f
