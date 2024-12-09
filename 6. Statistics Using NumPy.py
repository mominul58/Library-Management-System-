import pandas as pd
import numpy as np

# Load the data
csv_file = "library_data.csv"
df = pd.read_csv(csv_file)

def total_books():
    """Calculate the total number of books in the library."""
    total = np.size(df["Book ID"])
    print(f"Total number of books in the library: {total}")

def most_borrowed_genre():
    """Identify the most borrowed genre."""
    borrowed_books = df[df["Borrower"].notnull()]
    genre_counts = borrowed_books["Genre"].value_counts()
    if not genre_counts.empty:
        most_borrowed = genre_counts.idxmax()
        print(f"The most borrowed genre is: {most_borrowed}")
    else:
        print("No books have been borrowed yet.")

def average_borrowing_duration():
    """
    Analyze borrowing trends (average borrowing duration).
    Assuming the dataset has a column 'Borrowing Duration' in days.
    """
    if "Borrowing Duration" in df.columns:
        durations = df["Borrowing Duration"].dropna().values
        avg_duration = np.mean(durations)
        print(f"The average borrowing duration is: {avg_duration:.2f} days")
    else:
        print("The dataset does not include borrowing duration data.")

# Menu for testing the functionality
while True:
    print("\n--- Library Statistics Using NumPy ---")
    print("1. Total Number of Books")
    print("2. Most Borrowed Genre")
    print("3. Average Borrowing Duration")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        total_books()
    elif choice == 2:
        most_borrowed_genre()
    elif choice == 3:
        average_borrowing_duration()
    elif choice == 4:
        print("Exiting Library Statistics System.")
        break
    else:
        print("Invalid choice. Please try again.")
