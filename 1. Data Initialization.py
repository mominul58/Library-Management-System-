#part 1: Use a CSV file to store initial library data:

import csv

# Library data
library_data = {
    "Book ID": [1, 2, 3, 4, 5],
    "Title": ["Pather Panchali", "Chokher Bali", "Padma Nadir Majhi", "Kobor", "Shaheb Bibi Golam"],
    "Author": ["Bibhutibhushan Bandyopadhyay", "Rabindranath Tagore", "Manik Bandopadhyay", "Jasimuddin", "Bimal Mitra"],
    "Genre": ["Drama", "Social Drama", "Fiction", "Tragedy", "Historical Fiction"],
    "Availability": ["Yes", "Yes", "No", "Yes", "No"],
    "Borrower": [None, "Asif", "folik", None, "Rasel"]
}

# CSV file name
csv_file = "library_data.csv"

# Writing data to CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(library_data.keys())
    
    # Write the rows
    for i in range(len(library_data["Book ID"])):
        writer.writerow([
            library_data["Book ID"][i],
            library_data["Title"][i],
            library_data["Author"][i],
            library_data["Genre"][i],
            library_data["Availability"][i],
            library_data["Borrower"][i]
        ])

print(f"Library data has been saved to {csv_file}.")

#Part 2: Load the data into a Pandas DataFrame for processing.

import pandas as pd
csv_file = "library_data.csv"
df = pd.read_csv(csv_file)

print("Library Data:")
print(df)
