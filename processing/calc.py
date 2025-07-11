import pandas as pd
import os

def _load_data():
    """Helper function to load data with error handling"""
    file_path = "data/Book1.xlsx"
    if not os.path.exists(file_path):
        return None
    try:
        return pd.read_excel(file_path)
    except Exception:
        return None

def total_martyr_count():
    # Load fresh data each time
    df = _load_data()
    if df is None:
        return 0
    
    # Specify the column name to search for
    target_column_name = "Martyr Count"

    if target_column_name in df.columns:
        # Sum the values in the specified column
        total = df[target_column_name].sum()
        return total
    else:
        print(f"Column '{target_column_name}' not found.")
        return 0


def total_injured_count():
    # Load fresh data each time
    df = _load_data()
    if df is None:
        return 0
    
    # Specify the column name to search for
    target_column_name = "Injured Count"

    if target_column_name in df.columns:
        # Sum the values in the specified column
        total = df[target_column_name].sum()
        return total
    else:
        print(f"Column '{target_column_name}' not found.")
        return 0


def total_martyr_injured_count():
    return total_martyr_count() + total_injured_count()


# def most_damaged_region():
#     #Add damaged house count for each region
#     # then conclude that the one with the highest
#     # count is the most damaged and is most likely dangerous to live in.


# def least_damaged_region():
#     # Add damaged house count for each region
#     # then conclude that the one with the lowest
#     # count is the least damaged and is probably the most habitable.
#
# def most_victim_dates():
#     #Add all the martyr and injured count on a
#     # specific date.
#
#
# def attack_type_count():
#     #Sum attacks of each type.
#
# def martyr_percentage_by_region(region):
#     #Calculate the percentage of the martyrs in a given region.

