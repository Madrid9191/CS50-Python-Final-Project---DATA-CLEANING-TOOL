import pandas as pd
import pytest
from unittest.mock import patch
from project import remove_duplicates, handle_missing, convert_dtypes, strip_spaces, capitalize_text

@pytest.fixture
def sample_df():

    data = {
        "ID": ["1A", "2A", "3A", "3A", "4A", "5A", "6A"],
        "name": ["  juan  ", "ana", "LUIS", "LUIS", "carla ", "sofia", "PEDRO"],
        "age": [25, 30, 25, 25, None, 28, 40],
        "height": [1.75, None, 1.80, 1.80, 1.65, 1.70, 1.85],
        "date_of_birth": ["1998-05-12", "1993-07-21", "1998-05-12", "1998-05-12", "2001-02-03", "1995-11-09", ""],
        "city": ["  mexico", "Argentina", " mexico", " mexico", " chile", "PERU", " colombia"]
    }
    return pd.DataFrame(data)

def test_remove_duplicates(sample_df):
    with patch("builtins.input", side_effect=["ID", "No"]):
        cleaned = remove_duplicates(sample_df)
        assert cleaned.shape[0] < sample_df.shape[0]

def test_handle_missing(sample_df):

    cleaned = handle_missing(sample_df)
    assert cleaned.isnull().sum().sum() == 0

def test_convert_dtypes_int(sample_df):

    with patch("builtins.input", side_effect=["age", "int", "No"]):
        cleaned = convert_dtypes(sample_df.copy())
        assert pd.api.types.is_integer_dtype(cleaned["age"]) or pd.api.types.is_float_dtype(cleaned["age"])

def test_convert_dtypes_datetime(sample_df):

    with patch("builtins.input", side_effect=["date_of_birth", "datetime", "No"]):
        cleaned = convert_dtypes(sample_df.copy())
        assert pd.api.types.is_datetime64_any_dtype(cleaned["date_of_birth"])

def test_strip_spaces(sample_df):

    cleaned = strip_spaces(sample_df.copy())
    assert all(not str(x).startswith(" ") and not str(x).endswith(" ") for x in cleaned["name"])

def test_capitalize_text(sample_df):

    with patch("builtins.input", side_effect=["name, city", "No"]):
        cleaned = capitalize_text(sample_df.copy())
        assert cleaned["name"].iloc[5] == "Sofia"
        assert cleaned["city"].iloc[5] == "Peru"
