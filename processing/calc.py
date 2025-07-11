import pandas as pd
import os

# Load the Excel file
# df = pd.read_excel("data/Book1.xlsx")

DATA_FILE = "data/Book1.xlsx"


def _load_df():
    """Safely load the Excel file and return a cleaned DataFrame.

    If the file does not exist yet (e.g. first application run), an empty
    DataFrame with the expected schema is returned instead of raising an
    exception. All numeric columns are coerced to proper numeric dtype so
    that arithmetic operations like sum() behave correctly even when the
    underlying Excel values are stored as strings.
    """
    if not os.path.exists(DATA_FILE):
        # Return empty DataFrame with correct columns so subsequent code works
        return pd.DataFrame(
            columns=[
                "Date",
                "Region",
                "Martyr Count",
                "Injured Count",
                "Damaged Homes Count",
                "Attack Type",
            ]
        )

    df = pd.read_excel(DATA_FILE)

    # Coerce numeric columns to numbers, turning invalid entries into NaN so they
    # are ignored by sum() and other arithmetic ops.
    for col in ["Martyr Count", "Injured Count", "Damaged Homes Count"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


# Update the public API to use the freshly-loaded and cleaned DataFrame each time

def total_martyr_count():
    df = _load_df()
    return df["Martyr Count"].sum() if "Martyr Count" in df.columns else 0


def total_injured_count():
    df = _load_df()
    return df["Injured Count"].sum() if "Injured Count" in df.columns else 0


def total_martyr_injured_count():
    # Re-use the two helper functions so we only have one place where the
    # arithmetic/edge-case handling logic lives.
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

