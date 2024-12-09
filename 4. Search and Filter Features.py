import pandas as pd

# Load the data
csv_file = "library_data.csv"
df = pd.read_csv(csv_file)

def search_books():
    """Search for books by title, author, or genre."""
    print("\nSearch by:")
    print("1. Title")
    print("2. Author")
    print("3. Genre")
    choice = int(input("Enter your choice: "))
    
    query = input("Enter your search term: ").strip().lower()
    
    if choice == 1:
        results = df[df["Title"].str.lower().str.contains(query, na=False)]
    elif choice == 2:
        results = df[df["Author"].str.lower().str.contains(query, na=False)]
    elif choice == 3:
        results = df[df["Genre"].str.lower().str.contains(query, na=False)]
    else:
        print("Invalid choice. Returning to menu.")
        return
    
    if not results.empty:
        print("\nSearch Results:")
        print(results)
    else:
        print("No books found matching your search.")

def filter_books():
    """Filter books based on availability or borrower."""
    print("\nFilter by:")
    print("1. Show only available books")
    print("2. List books borrowed by a specific user")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        available_books = df[df["Availability"] == "Yes"]
        print("\nAvailable Books:")
        print(available_books)
    elif choice == 2:
        borrower = input("Enter the borrower's name: ").strip().lower()
        borrowed_books = df[df["Borrower"].str.lower().fillna("").str.contains(borrower, na=False)]
        
        if not borrowed_books.empty:
            print(f"\nBooks borrowed by {borrower.capitalize()}:")
            print(borrowed_books)
        else:
            print(f"No books found borrowed by {borrower.capitalize()}.")
    else:
        print("Invalid choice. Returning to menu.")

# Menu for testing the functionality
while True:
    print("\n--- Search and Filter Features ---")
    print("1. Search for Books")
    print("2. Filter Books")
    print("3. View Inventory")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        search_books()
    elif choice == 2:
        filter_books()
    elif choice == 3:
        print(df)
    elif choice == 4:
        print("Exiting Search and Filter System.")
        break
    else:
        print("Invalid choice. Please try again.")
