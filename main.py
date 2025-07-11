from openpyxl import Workbook
import openpyxl
import tkinter as tk
from tkinter import messagebox
import os

from processing.calc import *


def ensure_data_directory():
    """Ensure the data directory exists"""
    if not os.path.exists("data"):
        os.makedirs("data")


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
    try:
        martyr_count_int = int(martyr_count)
        injured_count_int = int(injured_count)
        damaged_homes_count_int = int(damaged_homes_count)
        
        if martyr_count_int < 0 or injured_count_int < 0 or damaged_homes_count_int < 0:
            messagebox.showwarning("Input Error", "Counts cannot be negative!")
            return
    except ValueError:
        messagebox.showwarning("Input Error", "Martyr Count, Injured Count, and Damaged Homes Count must be numbers!")
        return

    try:
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
        sheet.append([date, region, martyr_count_int, injured_count_int, damaged_homes_count_int, attack_type])
        workbook.save("data/Book1.xlsx")
        messagebox.showinfo("Success", "Data saved successfully!")
        date_entry.delete(0, tk.END)
        region_entry.delete(0, tk.END)
        martyr_count_entry.delete(0, tk.END)
        injured_count_entry.delete(0, tk.END)
        damaged_homes_count_entry.delete(0, tk.END)
        attack_type_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


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


tk.Label(root, text='Total Martyr Count: ').grid(row=7, column=0, padx=15, pady=10)
tk.Label(root, text=total_martyr_count()).grid(row=7, column=1, padx=15, pady=10)

tk.Label(root, text='Total Injured Count: ').grid(row=8, column=0, padx=15, pady=10)
tk.Label(root, text=total_injured_count()).grid(row=8, column=1, padx=15, pady=10)

tk.Label(root, text='Total Victim Count: ').grid(row=9, column=0, padx=15, pady=10)
tk.Label(root, text=total_martyr_injured_count()).grid(row=9, column=1, padx=15, pady=10)


root.mainloop()
