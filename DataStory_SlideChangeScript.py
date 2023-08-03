# Mike Bonsignore
# CIS DataStory Research
# Towson University Department of Computer & Information Sciences
# 7/30/23

# The purpose of this script is to organize and condense the large participant recording files
# into a collection of timestamps at which the participant moves on to the next chart.
# There are 4 charts total thus there will be 4 timestamps outputted. As of (7/30/23) the output
# is not formatted exactly as intended, however it is functionally gathering the transitional time stamps.

import pandas as pd

def analyze_csv_file(csv_file, column_names, output_file):
    # Import the CSV file
    df = pd.read_csv(csv_file)
    
    # Check if the specified columns exist
    missing_columns = [col for col in column_names if col not in df.columns]
    if missing_columns:
        print(f"Columns {missing_columns} not found in the dataset.")
        return

    # Define the output text file
    with open(output_file, 'w') as f:
        slidenum = 0
        first_row = df.iloc[0]  # Get the first row of the DataFrame

        # Handle the very first row of each specified column
        timestamp = first_row["LocalTimeStamp"]
        for col_name in column_names:
            col_value = first_row[col_name]
            if pd.notna(col_value):
                slidenum += 1
                msg = "User changed slides"
                f.write(f"{timestamp}, {msg}, Slide number: {slidenum}\n")

        # Main loop for the rest of the rows
        last_row = True  # Initialize as True for the first iteration
        for idx, row in df.iterrows():
            timestamp = row["LocalTimeStamp"]
            for col_name in column_names:
                col_value = row[col_name]
                # If it's not the first row and the next value in the column is empty, save to the txt file
                if not last_row and pd.notna(col_value) and pd.isna(df.at[idx + 1, col_name]):
                    slidenum += 1
                    msg = "User changed slides"
                    f.write(f"{timestamp}, {msg}, Slide number: {slidenum}\n")
                last_row = idx == len(df) - 1
        # Last row
        if last_row:
            slidenum += 1
            msg = "User ended the test"
            f.write(f"{timestamp}, {msg}\n")

if __name__ == "__main__":
    csv_file = "P10.csv"
    column_names = ["AOI[Title]Hit", "AOI[Title]Hit_1", "AOI[Title]Hit_3", "AOI[Title]Hit_4"]
    output_file = csv_file + "output.txt"

    analyze_csv_file(csv_file, column_names, output_file)