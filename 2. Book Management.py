import pandas as pd

# Load the data
csv_file = "library_data.csv"
df = pd.read_csv(csv_file)

def save_to_csv():
    """Save the DataFrame back to the CSV file."""
    df.to_csv(csv_file, index=False)
    print("Changes have been saved to the CSV file.")

def add_book():
    """Add a new book to the inventory."""
    global df
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    genre = input("Enter Genre: ")
    availability = input("Is the book available? (Yes/No): ")
    borrower = input("Enter Borrower (or leave empty): ")
    borrower = borrower if borrower else None
    
    new_book = {
        "Book ID": book_id,
        "Title": title,
        "Author": author,
        "Genre": genre,
        "Availability": availability,
        "Borrower": borrower
    }
    
    df = pd.concat([df, pd.DataFrame([new_book])], ignore_index=True)
    print(f"Book '{title}' has been added to the inventory.")
    save_to_csv()

def remove_book():
    """Remove a book by its ID."""
    global df
    book_id = int(input("Enter the Book ID to remove: "))
    if book_id in df["Book ID"].values:
        df = df[df["Book ID"] != book_id]
        print(f"Book with ID {book_id} has been removed.")
        save_to_csv()
    else:
        print(f"No book found with ID {book_id}.")

def update_book():
    """Update book details."""
    global df
    book_id = int(input("Enter the Book ID to update: "))
    if book_id in df["Book ID"].values:
        print("What would you like to update?")
        print("1. Availability")
        print("2. Borrower")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            availability = input("Enter new availability status (Yes/No): ")
            df.loc[df["Book ID"] == book_id, "Availability"] = availability
            print(f"Availability of book ID {book_id} has been updated.")
        elif choice == 2:
            borrower = input("Enter new borrower (or leave empty): ")
            borrower = borrower if borrower else None
            df.loc[df["Book ID"] == book_id, "Borrower"] = borrower
            print(f"Borrower of book ID {book_id} has been updated.")
        else:
            print("Invalid choice.")
        save_to_csv()
    else:
        print(f"No book found with ID {book_id}.")

# Menu for testing the functionality
while True:
    print("\n--- Library Management ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Update Book")
    print("4. View Inventory")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        remove_book()
    elif choice == 3:
        update_book()
    elif choice == 4:
        print(df)
    elif choice == 5:
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
