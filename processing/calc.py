import pandas as pd
import os

# Load the Excel file with error handling
def load_data():
    try:
        if os.path.exists("data/Book1.xlsx"):
            return pd.read_excel("data/Book1.xlsx")
        else:
            return pd.DataFrame(columns=['Date', 'Region', 'Martyr Count', 'Injured Count', 'Damaged Homes Count', 'Attack Type'])
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame(columns=['Date', 'Region', 'Martyr Count', 'Injured Count', 'Damaged Homes Count', 'Attack Type'])

df = load_data()


def total_martyr_count():
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
    return total_martyr_count()+total_injured_count()


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

