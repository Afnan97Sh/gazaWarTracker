import pandas as pd
import os

# Load the Excel file only if it exists
def load_data():
    try:
        if os.path.exists("data/Book1.xlsx"):
            return pd.read_excel("data/Book1.xlsx")
        else:
            # Return empty DataFrame with correct columns if file doesn't exist
            return pd.DataFrame(columns=['Date', 'Region', 'Martyr Count', 'Injured Count', 'Damaged Homes Count', 'Attack Type'])
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame(columns=['Date', 'Region', 'Martyr Count', 'Injured Count', 'Damaged Homes Count', 'Attack Type'])

# Initialize df
df = load_data()


def total_martyr_count():
    # Reload data to get latest values
    global df
    df = load_data()
    
    # Specify the column name to search for
    target_column_name = "Martyr Count"

    if target_column_name in df.columns and not df.empty:
        # Sum the values in the specified column
        total = df[target_column_name].sum()
        return total
    else:
        return 0


def total_injured_count():
    # Reload data to get latest values
    global df
    df = load_data()
    
    # Specify the column name to search for
    target_column_name = "Injured Count"

    if target_column_name in df.columns and not df.empty:
        # Sum the values in the specified column
        total = df[target_column_name].sum()
        return total
    else:
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

