import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations():
    """Create all visualizations with proper error handling"""
    # Check if file exists
    file_path = "data/Book1.xlsx"
    if not os.path.exists(file_path):
        print(f"Error: Data file '{file_path}' not found.")
        print("Please run the main application first to create some data.")
        return
    
    try:
        # Read Excel file
        df = pd.read_excel(file_path)
        
        # Check if dataframe has data
        if df.empty:
            print("Warning: Data file exists but contains no data.")
            return
            
        # Check if required columns exist
        required_columns = ["Date", "Region", "Martyr Count", "Injured Count", "Damaged Homes Count", "Attack Type"]
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Error: Missing required columns: {missing_columns}")
            return
            
    except Exception as e:
        print(f"Error reading data file: {e}")
        return

    try:
        # Convert date column
        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

        # Line Chart – Martyr count by date
        plt.figure(figsize=(10, 6))
        sns.lineplot(x="Date", y="Martyr Count", data=df, marker="o")
        plt.title("Martyrs by Date")
        plt.xlabel("Date")
        plt.ylabel("Martyr Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Bar Chart – Most damaged regions
        region_damage = df.groupby("Region")["Damaged Homes Count"].sum().sort_values(ascending=False)

        if not region_damage.empty:
            plt.figure(figsize=(10, 6))
            sns.barplot(x=region_damage.values, y=region_damage.index)
            plt.title("Most Damaged Regions")
            plt.xlabel("Number of Damaged Homes")
            plt.ylabel("Region")
            plt.tight_layout()
            plt.show()
        else:
            print("Warning: No region damage data to plot.")

        # Pie Chart Attack type distribution
        attack_distribution = df["Attack Type"].value_counts()

        if not attack_distribution.empty:
            plt.figure(figsize=(6, 6))
            plt.pie(attack_distribution, labels=attack_distribution.index, autopct='%1.1f%%', startangle=140)
            plt.title("Attack Type Distribution")
            plt.tight_layout()
            plt.show()
        else:
            print("Warning: No attack type data to plot.")

        # Bar chart of days with the highest martyr counts.
        if len(df) >= 5:
            top_days = df.sort_values("Martyr Count", ascending=False).head(5)
        else:
            top_days = df.sort_values("Martyr Count", ascending=False)
            
        if not top_days.empty:
            plt.figure(figsize=(8, 6))
            sns.barplot(x=top_days["Date"].dt.strftime('%Y-%m-%d'), y=top_days["Martyr Count"])
            plt.title("Top Deadliest Days")
            plt.xlabel("Date")
            plt.ylabel("Martyr Count")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("Warning: No martyr count data to plot.")

        # Heatmap of Damaged Homes by Region and Attack Type
        try:
            pivot_table = df.pivot_table(
                index="Region", columns="Attack Type", values="Damaged Homes Count", aggfunc="sum", fill_value=0
            )

            if not pivot_table.empty:
                plt.figure(figsize=(10, 6))
                sns.heatmap(pivot_table, annot=True, fmt="d", cmap="Reds")
                plt.title("Damaged Homes by Region and Attack Type")
                plt.tight_layout()
                plt.show()
            else:
                print("Warning: No data available for heatmap.")
        except Exception as e:
            print(f"Warning: Could not create heatmap: {e}")

    except Exception as e:
        print(f"Error creating visualizations: {e}")

if __name__ == "__main__":
    create_visualizations()
