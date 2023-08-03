# Mike Bonsignore
# CIS DataStory Research
# Towson University Department of Computer & Information Sciences
# 7/25/23

# The purpose of this script is to organize and condense the large participant recording files
# into a collection of timestamps at which the participant changes between any AOI's during the recording.
# This progam as of (7/27/23) Filters each row of AOIs by printing a row if it is different than the previous row
# so that only the rows that indicate changes in AOI are printed along with their timestamp and index.

import pandas as pd

# method to save a row to the output txt file
def save_row_to_file(file_path, index, row, additional_column_value):
    with open(file_path, 'a') as file:
        row_str = '\t'.join(map(str, [index] + list(row) + [additional_column_value]))
        file.write(row_str + '\n')

# Begin main
def main():
    csv_file_path = "P10.csv"  ##### Replace 'P10.csv' with the name of any participant's file to be filtered #####
    df = pd.read_csv(csv_file_path)

    # subset of columns containing AOIs
    AOIcols = ['AOI[Title]Hit',
                'AOI[Main Data]Hit',
                'AOI[Rectangle 4]Hit',
                'AOI[Y axis]Hit',
                'AOI[X axis]Hit',
                'AOI[Help text]Hit',
                'AOI[Main chart]Hit',
                'AOI[Title]Hit_1',
                'AOI[Y axis (Solar)]Hit',
                'AOI[Y axis (Temp)]Hit',
                'AOI[X axis]Hit_2',
                'AOI[Title]Hit_3',
                'AOI[AI and AN Reading Data]Hit',
                'AOI[Asian Reading Data]Hit',
                'AOI[Black Reading Data]Hit',
                'AOI[Hispanic Reading Data]Hit',
                'AOI[White Reading Data]Hit',
                'AOI[AI and AN Math Data]Hit',
                'AOI[Asian Math Data]Hit',
                'AOI[Black Math Data]Hit',
                'AOI[Hispanic Math Data]Hit',
                'AOI[White Math Data]Hit',
                'AOI[Title]Hit_4',
                'AOI[Key]Hit',
                'AOI[Main Chart]Hit.1',
                'AOI[Y axis]Hit_5',
                'AOI[Chart Help Text]Hit']

    # Extract timestamps
    timestamps = df['LocalTimeStamp']
    # keep only AOI columns
    df = df[AOIcols]

    # create output file
    output_file_path = csv_file_path + "output.txt"

    # iteration comparing each row with the previous row
    prev_row = None
    for index, row in df.iterrows():
        if prev_row is not None and not prev_row.equals(row):
            # Get the corresponding timestamp for the current row
            additional_column_value = timestamps.iloc[index]
            # Print the row to the output file with the index and timestamp
            save_row_to_file(output_file_path, index, row, additional_column_value)
        # next row and repeat
        prev_row = row

# End program
if __name__ == "__main__":
    main()