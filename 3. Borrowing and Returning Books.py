import pandas as pd

# Load the data
csv_file = "library_data.csv"
df = pd.read_csv(csv_file)

def save_to_csv():
    """Save the DataFrame back to the CSV file."""
    df.to_csv(csv_file, index=False)
    print("Changes have been saved to the CSV file.")

def borrow_book():
    """Borrow a book."""
    global df
    book_id = int(input("Enter the Book ID to borrow: "))
    if book_id in df["Book ID"].values:
        book_row = df.loc[df["Book ID"] == book_id]
        availability = book_row["Availability"].values[0]
        
        if availability == "Yes":
            borrower = input("Enter the borrower's name: ")
            df.loc[df["Book ID"] == book_id, "Borrower"] = borrower
            df.loc[df["Book ID"] == book_id, "Availability"] = "No"
            print(f"Book ID {book_id} has been borrowed by {borrower}.")
            save_to_csv()
        else:
            print(f"Book ID {book_id} is currently unavailable.")
    else:
        print(f"No book found with ID {book_id}.")

def return_book():
    """Return a book."""
    global df
    book_id = int(input("Enter the Book ID to return: "))
    if book_id in df["Book ID"].values:
        book_row = df.loc[df["Book ID"] == book_id]
        availability = book_row["Availability"].values[0]
        
        if availability == "No":
            df.loc[df["Book ID"] == book_id, "Borrower"] = None
            df.loc[df["Book ID"] == book_id, "Availability"] = "Yes"
            print(f"Book ID {book_id} has been returned and marked as available.")
            save_to_csv()
        else:
            print(f"Book ID {book_id} is already marked as available.")
    else:
        print(f"No book found with ID {book_id}.")

# Menu for testing the functionality
while True:
    print("\n--- Borrowing and Returning Books ---")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. View Inventory")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        borrow_book()
    elif choice == 2:
        return_book()
    elif choice == 3:
        print(df)
    elif choice == 4:
        print("Exiting Borrowing and Returning System.")
        break
    else:
        print("Invalid choice. Please try again.")
