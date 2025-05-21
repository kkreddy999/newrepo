import csv

class Book:
    def __init__(self, book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        return f"{self.book_id},{self.title},{self.author},{self.is_available}"

class User:
    def __init__(self, username):
        self.username = username
        self.borrowed_books = []

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.load_books()
        self.load_users()

    def load_books(self):
        try:
            with open("books.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        book = Book(row[0], row[1], row[2], row[3] == 'True')
                        self.books.append(book)
        except FileNotFoundError:
            pass

    def save_books(self):
        with open("books.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([book.book_id, book.title, book.author, book.is_available])

    def load_users(self):
        try:
            with open("users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        user = User(row[0])
                        user.borrowed_books = row[1:]
                        self.users.append(user)
        except FileNotFoundError:
            pass

    def save_users(self):
        with open("users.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for user in self.users:
                writer.writerow([user.username] + user.borrowed_books)

    def add_book(self):
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        self.books.append(Book(book_id, title, author))
        self.save_books()
        print("Book added successfully.")

    def delete_book(self):
        book_id = input("Enter book ID to delete: ")
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()
        print("Book deleted successfully.")

    def search_books(self):
        keyword = input("Enter keyword to search: ")
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(f"{book.book_id}: {book.title} by {book.author} - {'Available' if book.is_available else 'Not Available'}")
                found = True
        if not found:
            print("No books found.")

    def borrow_book(self):
        username = input("Enter your username: ")
        book_id = input("Enter book ID to borrow: ")
        user = self.get_user(username)
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.is_available = False
                user.borrowed_books.append(book_id)
                self.save_books()
                self.save_users()
                print(f"{book.title} has been borrowed.")
                return
        print("Book not available.")

    def return_book(self):
        username = input("Enter your username: ")
        book_id = input("Enter book ID to return: ")
        user = self.get_user(username)
        if book_id in user.borrowed_books:
            user.borrowed_books.remove(book_id)
            for book in self.books:
                if book.book_id == book_id:
                    book.is_available = True
            self.save_books()
            self.save_users()
            print("Book returned successfully.")
        else:
            print("You didn't borrow this book.")

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        new_user = User(username)
        self.users.append(new_user)
        return new_user

def main():
    system = LibrarySystem()
    while True:
        print("\nLibrary Menu")
        print("1. Add Book\n2. Delete Book\n3. Search Book\n4. Borrow Book\n5. Return Book\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            system.add_book()
        elif choice == '2':
            system.delete_book()
        elif choice == '3':
            system.search_books()
        elif choice == '4':
            system.borrow_book()
        elif choice == '5':
            system.return_book()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
