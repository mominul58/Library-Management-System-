import pandas as pd
import re
import matplotlib.pyplot as plt

# Load the data
csv_file = "library_data.csv"
df = pd.read_csv(csv_file)

def validate_book_id(book_id):
    """Validate book ID format (e.g., BK-001)."""
    if re.match(r"^BK-\d{3}$", book_id):
        return True
    return False

def add_book_with_validation():
    """Add a new book with validated book ID."""
    global df
    book_id = input("Enter Book ID (format BK-001): ").strip()
    if not validate_book_id(book_id):
        print("Invalid Book ID format. Please use format BK-001.")
        return

    try:
        if book_id in df["Book ID"].values:
            print("Book ID already exists. Please enter a unique ID.")
            return
    except KeyError:
        pass  # Handle missing 'Book ID' column gracefully

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

def handle_invalid_book_id(book_id):
    """Gracefully handle invalid or missing book IDs."""
    try:
        if book_id not in df["Book ID"].values:
            print(f"No book found with ID {book_id}. Please try again.")
            return False
        return True
    except KeyError:
        print("Book ID column is missing in the data.")
        return False

def save_to_csv():
    """Save the DataFrame back to the CSV file."""
    df.to_csv(csv_file, index=False)
    print("Changes have been saved to the CSV file.")

def display_genre_chart():
    """Display a bar chart of the number of books in each genre."""
    genre_counts = df["Genre"].value_counts()
    genre_counts.plot(kind="bar", color="skyblue", title="Number of Books by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Number of Books")
    plt.show()

def display_availability_pie_chart():
    """Display a pie chart of book availability."""
    availability_counts = df["Availability"].value_counts()
    availability_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["green", "red"])
    plt.title("Availability Status (Available vs Borrowed)")
    plt.ylabel("")  # Hide y-axis label
    plt.show()

# Menu for testing the functionality
while True:
    print("\n--- Advanced Features ---")
    print("1. Add Book with Validation")
    print("2. Check Book ID Validity")
    print("3. Display Genre Bar Chart")
    print("4. Display Availability Pie Chart")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book_with_validation()
    elif choice == 2:
        book_id = input("Enter Book ID to validate: ")
        if validate_book_id(book_id):
            print("Valid Book ID.")
        else:
            print("Invalid Book ID format.")
    elif choice == 3:
        display_genre_chart()
    elif choice == 4:
        display_availability_pie_chart()
    elif choice == 5:
        print("Exiting Advanced Features.")
        break
    else:
        print("Invalid choice. Please try again.")
