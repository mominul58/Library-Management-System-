#Use a CSV file to store initial library data


import pandas as pd

# Sample initial data
library_data = {
    "Book ID": [1, 2, 3, 4, 5],
    "Title": ["Pather Panchali", "Chokher Bali", "Padma Nadir Majhi", "Kobor", "Shaheb Bibi Golam"],
    "Author": ["Bibhutibhushan Bandyopadhyay", "Rabindranath Tagore", "Manik Bandopadhyay", "Jasimuddin", "Bimal Mitra"],
    "Genre": ["Drama", "Social Drama", "Fiction", "Tragedy", "Historical Fiction"],
    "Availability": ["Yes", "Yes", "No", "Yes", "No"],
    "Borrower": [None, "Asif", "folik", None, "Rasel"]
}

# Create a Pandas DataFrame
df = pd.DataFrame(library_data)

# Save the DataFrame to a CSV file
csv_file = "library_data.csv"
df.to_csv(csv_file, index=False)
# print(f"Library data has been saved to {csv_file}.")

# Load the CSV file into a DataFrame
loaded_df = pd.read_csv(csv_file)

# Display the loaded data
print("Library Data:")
print(loaded_df)
