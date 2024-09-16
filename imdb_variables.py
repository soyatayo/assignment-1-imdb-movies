
file_path = r'C:\Users\sharo\OneDrive\Documents\Intro to informatics\imdb-movies-dataset.csv'

import pandas as pd


df = pd.read_csv(file_path)


print("List of variables and their data types:\n")
print(df.dtypes)

with open("output_variable_data_types.txt", "w") as file:
    file.write("List of variables and their data types:\n")
    for var, dtype in df.dtypes.items():
        file.write(f"{var}: {dtype}\n")

print("\nData types have been written to output_variable_data_types.txt")

