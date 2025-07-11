# War Data Registry

A Python application for recording and analyzing war-related data including casualties, injuries, and property damage.

## Features

- **Data Entry**: Add war incident data including date, region, casualty counts, and attack types
- **Statistics**: View total casualty and injury counts
- **Visualization**: Generate charts and graphs from the data
- **Data Storage**: Excel-based data storage

## Files

- `main.py` - GUI application (requires tkinter)
- `main_cli.py` - Command-line interface version
- `visualize.py` - Data visualization script
- `processing/calc.py` - Calculation functions
- `data/Book1.xlsx` - Data storage file

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface (Recommended)
```bash
python3 main_cli.py
```

### GUI Interface (requires tkinter)
```bash
python3 main.py
```

### Generate Visualizations
```bash
python3 visualize.py
```

## Bugs Fixed

### 1. Missing Dependencies
- **Issue**: Missing required Python packages (openpyxl, pandas, matplotlib, seaborn)
- **Fix**: Created `requirements.txt` with all necessary dependencies

### 2. Missing tkinter Module
- **Issue**: GUI application requires tkinter which isn't available in all environments
- **Fix**: Created `main_cli.py` as a command-line alternative

### 3. Missing Error Handling in calc.py
- **Issue**: Functions would crash if Excel file doesn't exist
- **Fix**: Added proper error handling and fallback to empty DataFrame

### 4. Missing Error Handling in visualize.py
- **Issue**: Script would crash if data file is missing or empty
- **Fix**: Added comprehensive error checking and user-friendly messages

### 5. Missing Data Directory Creation
- **Issue**: Application would fail if data directory doesn't exist
- **Fix**: Added `ensure_data_directory()` function to create directory if needed

### 6. Input Validation Issues
- **Issue**: No validation for numeric inputs or negative values
- **Fix**: Added proper input validation for all numeric fields

### 7. Matplotlib Display Issues
- **Issue**: `plt.show()` doesn't work in headless environments
- **Fix**: Changed to save charts as PNG files instead of displaying them

### 8. Return Value Issues
- **Issue**: Functions returned None instead of 0 when data is missing
- **Fix**: Added proper return values for all calculation functions

## Data Format

The application expects data in the following format:
- Date: DD/MM/YYYY
- Region: Text
- Martyr Count: Integer (≥ 0)
- Injured Count: Integer (≥ 0)
- Damaged Homes Count: Integer (≥ 0)
- Attack Type: Text

## Generated Charts

The visualization script creates the following PNG files:
- `martyrs_by_date.png` - Line chart of casualties over time
- `most_damaged_regions.png` - Bar chart of most affected regions
- `attack_type_distribution.png` - Pie chart of attack types
- `top_5_deadliest_days.png` - Bar chart of worst days
- `damaged_homes_heatmap.png` - Heatmap of damage by region and attack type
