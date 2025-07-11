from openpyxl import Workbook
import openpyxl
import os

# Try to import tkinter with error handling
try:
    import tkinter as tk
    from tkinter import messagebox
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False
    print("Warning: tkinter is not available. GUI cannot be displayed.")

from processing.calc import *


def validate_numeric_input(value, field_name):
    """Validate that input is a non-negative number"""
    try:
        num = float(value)
        if num < 0:
            messagebox.showwarning("Input Error", f"{field_name} cannot be negative!")
            return False
        return True
    except ValueError:
        messagebox.showwarning("Input Error", f"{field_name} must be a valid number!")
        return False


def update_statistics():
    """Update the statistics labels with current data"""
    martyr_label.config(text=total_martyr_count())
    injured_label.config(text=total_injured_count())
    total_label.config(text=total_martyr_injured_count())


def submit_data():
    date = date_entry.get()
    region = region_entry.get()
    martyr_count = martyr_count_entry.get()
    injured_count = injured_count_entry.get()
    damaged_homes_count = damaged_homes_count_entry.get()
    attack_type = attack_type_entry.get()

    if not date or not region or not martyr_count or not injured_count or not damaged_homes_count or not attack_type:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Validate numeric inputs
    if not validate_numeric_input(martyr_count, "Martyr Count"):
        return
    if not validate_numeric_input(injured_count, "Injured Count"):
        return
    if not validate_numeric_input(damaged_homes_count, "Damaged Homes Count"):
        return

    try:
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        # Open or create an Excel file
        try:
            workbook = openpyxl.load_workbook("data/Book1.xlsx")
            sheet = workbook.active
        except FileNotFoundError:
            workbook = Workbook()
            sheet = workbook.active
            # Add headers if creating a new file
            sheet.append(['Date', 'Region', "Martyr Count", 'Injured Count', 'Damaged Homes Count', 'Attack Type'])

        # Convert to proper numeric types
        martyr_count_num = int(float(martyr_count))
        injured_count_num = int(float(injured_count))
        damaged_homes_count_num = int(float(damaged_homes_count))

        # Append user data
        sheet.append([date, region, martyr_count_num, injured_count_num, damaged_homes_count_num, attack_type])
        workbook.save("data/Book1.xlsx")
        messagebox.showinfo("Success", "Data saved successfully!")
        
        # Clear entry fields
        date_entry.delete(0, tk.END)
        region_entry.delete(0, tk.END)
        martyr_count_entry.delete(0, tk.END)
        injured_count_entry.delete(0, tk.END)
        damaged_homes_count_entry.delete(0, tk.END)
        attack_type_entry.delete(0, tk.END)
        
        # Update statistics after saving
        update_statistics()
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def main():
    """Main function to run the GUI application"""
    if not TKINTER_AVAILABLE:
        print("Cannot run GUI application: tkinter is not available")
        return

    global root, date_entry, region_entry, martyr_count_entry, injured_count_entry
    global damaged_homes_count_entry, attack_type_entry
    global martyr_label, injured_label, total_label

    root = tk.Tk()
    root.title("War Data Registry")
    root.geometry("400x600")
    root.config(bg="light green")

    # Labels and Entry fields
    tk.Label(root, text="Date:").grid(row=0, column=0, padx=15, pady=10)
    date_entry = tk.Entry(root)
    date_entry.grid(row=0, column=1, padx=15, pady=10)

    tk.Label(root, text="Region:").grid(row=1, column=0, padx=15, pady=10)
    region_entry = tk.Entry(root)
    region_entry.grid(row=1, column=1, padx=15, pady=10)

    tk.Label(root, text="Martyr Count:").grid(row=2, column=0, padx=15, pady=10)
    martyr_count_entry = tk.Entry(root)
    martyr_count_entry.grid(row=2, column=1, padx=15, pady=10)

    tk.Label(root, text="Injured Count:").grid(row=3, column=0, padx=15, pady=10)
    injured_count_entry = tk.Entry(root)
    injured_count_entry.grid(row=3, column=1, padx=15, pady=10)

    tk.Label(root, text="Damaged Homes Count:").grid(row=4, column=0, padx=15, pady=10)
    damaged_homes_count_entry = tk.Entry(root)
    damaged_homes_count_entry.grid(row=4, column=1, padx=15, pady=10)

    tk.Label(root, text="Attack Type:").grid(row=5, column=0, padx=15, pady=10)
    attack_type_entry = tk.Entry(root)
    attack_type_entry.grid(row=5, column=1, padx=15, pady=10)

    tk.Button(root, text="Submit", fg="white", bg="red", command=submit_data).grid(row=6, column=1, columnspan=2, pady=10)

    # Statistics section with dynamic labels
    tk.Label(root, text='Total Martyr Count: ').grid(row=7, column=0, padx=15, pady=10)
    martyr_label = tk.Label(root, text="0")
    martyr_label.grid(row=7, column=1, padx=15, pady=10)

    tk.Label(root, text='Total Injured Count: ').grid(row=8, column=0, padx=15, pady=10)
    injured_label = tk.Label(root, text="0")
    injured_label.grid(row=8, column=1, padx=15, pady=10)

    tk.Label(root, text='Total Victim Count: ').grid(row=9, column=0, padx=15, pady=10)
    total_label = tk.Label(root, text="0")
    total_label.grid(row=9, column=1, padx=15, pady=10)

    # Add refresh button to update statistics
    tk.Button(root, text="Refresh Statistics", command=update_statistics).grid(row=10, column=1, columnspan=2, pady=10)

    # Initial load of statistics
    update_statistics()

    root.mainloop()


if __name__ == "__main__":
    main()
