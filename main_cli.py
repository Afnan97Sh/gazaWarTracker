from openpyxl import Workbook
import openpyxl
import os
from processing.calc import *


def ensure_data_directory():
    """Ensure the data directory exists"""
    if not os.path.exists("data"):
        os.makedirs("data")


def submit_data():
    print("=== War Data Registry ===")
    
    # Get user input
    date = input("Date (DD/MM/YYYY): ")
    region = input("Region: ")
    martyr_count = input("Martyr Count: ")
    injured_count = input("Injured Count: ")
    damaged_homes_count = input("Damaged Homes Count: ")
    attack_type = input("Attack Type: ")

    if not date or not region or not martyr_count or not injured_count or not damaged_homes_count or not attack_type:
        print("Error: All fields are required!")
        return

    try:
        # Convert numeric inputs
        martyr_count = int(martyr_count)
        injured_count = int(injured_count)
        damaged_homes_count = int(damaged_homes_count)
        
        # Ensure data directory exists
        ensure_data_directory()
        
        # Open or create an Excel file
        try:
            workbook = openpyxl.load_workbook("data/Book1.xlsx")
            sheet = workbook.active
        except FileNotFoundError:
            workbook = Workbook()
            sheet = workbook.active
            # Add headers if creating a new file
            sheet.append(['Date', 'Region', "Martyr Count", 'Injured Count', 'Damaged Homes Count', 'Attack Type'])

        # Append user data
        sheet.append([date, region, martyr_count, injured_count, damaged_homes_count, attack_type])
        workbook.save("data/Book1.xlsx")
        print("Data saved successfully!")
        
    except ValueError:
        print("Error: Martyr Count, Injured Count, and Damaged Homes Count must be numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")


def show_statistics():
    print("\n=== Current Statistics ===")
    print(f'Total Martyr Count: {total_martyr_count()}')
    print(f'Total Injured Count: {total_injured_count()}')
    print(f'Total Victim Count: {total_martyr_injured_count()}')


def main():
    while True:
        print("\n=== Menu ===")
        print("1. Add new data")
        print("2. Show statistics")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            submit_data()
        elif choice == "2":
            show_statistics()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()