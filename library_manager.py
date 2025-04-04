from collections import Counter
import json

def load_books():
    global library
    try:
        with open("library.json", "r") as file:
            library = json.load(file)
    except FileNotFoundError:
        print("No existing library found. Starting fresh.")
        library = []
    except json.JSONDecodeError:
        print("Error: library.json is corrupted. Starting with an empty library.")
        library = []


library = []
load_books()

book1 = {
    "title": "How to Win Friends and Influence People",
    "author": "Dale Carnegie",
    "year": 1936,
    "genre": "Self-Improvement & Motivation",
    "read": True
}
book2 = {
    "title": "Brave New World",
    "author": "Aldous Huxley",
    "year": 1932,
    "genre": "Fiction & Fantasy",
    "read": False
}
book3 = {
    "title": "And Then There Were None",
    "author": "Agatha Christie",
    "year": 1939,
    "genre": "Mystery & Thriller",
    "read": True
}
book4 = {
    "title": "Great Expectations",
    "author": "Charles Dickens",
    "year": 1861,
    "genre": "Classic Literature",
    "read": False
}
book5 = {
    "title": "The Intelligent Investor",
    "author": "Benjamin Graham",
    "year": 1949,
    "genre": "Business & Finance",
    "read": True
}


if not library: 
    for book in [book1, book2, book3, book4, book5]:
        
        if not any(existing_book['title'].lower() == book['title'].lower() for existing_book in library):
            library.append(book)



def add_book():
    while True:
        title = input("Enter the book title: ").strip()
        if title:
            break
        print("Title cannot be empty")

    while True:
        author = input("Enter the author:").strip()
        if author:
            break
        print("Author cannot be empty!")

    while True:
        try:
            year = int(input("Enter the publication year: "))
            if 1000 <= year <= 2025:
                break
            print("Please enter a valid year between 1000 and 2025.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the year.")
    
        
    genre = input("Enter the genre:").strip()

    while True:
        read_status = input("Have you read this book? (yes/no): ").strip().lower()
        if read_status in {"yes", "no"}:
           read =  read_status == "yes"
           break
        print("Please enter 'yes' or 'no'.")

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    print(f" '{title}' by {author} added successfully to library! \n")
    save_books()




def remove_book():
   if not library:
       print("Your library is empty! Nothing to remove. \n")
       return
   
   print("Available books in your library:")
   for book in library:
        print(f" - {book['title']}")

    
   title = input("\n Enter the title of the book you want to delete: ")

   for book in library:
        if book["title"].strip().lower() == title.strip().lower():
            library.remove(book)
            print(f"'{title}' has been removed from your library \n")
            save_books()
            return
        
   print(f"Book titled '{title}' not found in your library \n")



def find_book():

    if not library:
        print("Your library is empty! No books to search. \n")
        return
    
    title = input("Enter the book title you want to find: \n")
    
    for find in library:
        if find["title"].lower() == title.lower():
            print("\n Book found")
            print(f"Title: {find['title']}")
            print(f"Author: {find['author']}")
            print(f"Genre: {find['genre']}")
            print(f"Year: {find['year']}")
            print(f"Read: {'Yes' if find['read'] else 'No'} \n")
            return
        
    print(f"Book titled: {title} not found in your library. \n")




def show_all_books():
    if not library:
        print("Your library is empty! Add some books first \n")
        return
    

    print("Your Library Collection \n")
    for index, book in enumerate(library, start = 1):
        print(f"{index}. {book['title']} by {book['author']} ({book['year']})")
        print(f"    Genre: {book['genre']}")
        print(f"    Read: {'Yes' if book['read'] else 'No'}")
        print("-" * 40)




def library_stats():
    if not library:
        print("Your library is empty! Add some books first! \n")
        return
    
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    unread_books = total_books - read_books

    oldest_book = min(library, key=lambda book: book['year'])
    newest_book = max(library, key=lambda book: book['year'])

    genres = [book['genre'] for book in library]
    most_common_genre = Counter(genres).most_common(1)
    most_common_genre = most_common_genre[0][0] if most_common_genre else "Unknown"


    print("Library Statistics")
    print(f"Total Book: {total_books}")
    print(f"Books Read: {read_books}")
    print(f"Books Unread: {unread_books}")
    print(f"Oldest Book: {oldest_book['title']} ({oldest_book['year']}) by {oldest_book['author']}")
    print(f"Newest Book: {newest_book['title']} ({newest_book['year']}) by {newest_book['author']}")
    print(f"Most Common Genre:{most_common_genre}")
    print("-" * 40)




def update_read_status():
    title = input("Enter the book title you want to update: \n").strip()


    for book in library:
        if book['title'].lower() == title.lower():
            book['read'] = not book['read']
            status = "read" if book['read'] else 'not read'
            print(f"Updated: '{book['title']}' is now marked as {status}")
            save_books()
            return
        
    print(f"Book titled '{title}' not found.")



def save_books():
    try:
        with open("library.json", "w") as file:
            json.dump(library, file)
        print("Library saved successfully.")
    except IOError:
        print("Error: Unable to save the library file.")




def display_menu():
    while True:  
        print(""" 
            Welcome to your personal Library Manager
            1. Add a New Book
            2. Delete a Book
            3. Find a Book
            4. Show all Books
            5. Library Stats
            6. Update Read Status
            7. Quit
        """)

        choice = input("Enter your choice: ").strip()

        if choice.isdigit() and choice in {"1", "2", "3", "4", "5", "6", "7"}:
            return choice   # return valid choice
        
        print("Invalid Choice! Please enter a number between 1 and 7.")


while True:
    choice = display_menu()


    if choice == "1":
        add_book()

    elif choice == "2":
        remove_book()
    
    elif choice == "3":
        find_book()
        
    elif choice == "4":
        show_all_books()

    elif choice == "5":
        library_stats()

    elif choice == "6":
        update_read_status()
        
    elif choice == "7":
        save_books()
        print("Exiting the Program, Good Bye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")







