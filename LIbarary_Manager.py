import json

class LibraryManage:
    def __init__(self, filename="library.txt"):
        self.filename = filename
        self.library = []
        self.load_library()

    def load_library(self):
        try:
            with open(self.filename, 'r') as f:
                self.library = json.load(f)
            print("📂 Library loaded successfully!\n")
        except (FileNotFoundError, json.JSONDecodeError):
            print("📭 No existing library found. Starting fresh!\n")
            self.library = []

    def save_library(self):
        with open(self.filename, 'w') as f:
            json.dump(self.library, f, indent=4)
        print("💾 Library saved successfully!\n")

    def add_book(self):
        title = input("\n📚 Enter book title: ")
        author = input("✍️ Enter author: ")
        year = input("📅 Enter publication year: ")
        read_status = input("✅ Have you read this book? (y/n): ").lower()
        read = True if read_status == 'y' else False
        book = {"Title": title, "Author": author, "Year": year, "Read": read}
        self.library.append(book)
        print(f"✅ Book '{title}' added to your library!\n")
        self.save_library()

    def view_book(self):
        if not self.library:
            print("\n📭 Your library is empty.\n")
            return
        print("\n📚 Your Library:")
        for idx, book in enumerate(self.library, 1):
            status = "✔️ Read" if book['Read'] else "❌ Not Read"
            print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - {status}")
        print()

    def remove_book(self):
        self.view_book()
        if not self.library:
            return
        try:
            delete = int(input("\n🗑️ Enter the number of the book to remove: "))
            if 1 <= delete <= len(self.library):
                removed = self.library.pop(delete - 1)
                print(f"\n✅ Book '{removed['Title']}' removed successfully!\n")
                self.save_library()
            else:
                print("\n❌ Invalid number! Please try again.\n")
        except ValueError:
            print("\n❌ Please enter a valid number (1, 2, 3, ...).\n")

    def toggle_read_status(self):
        self.view_book()
        if not self.library:
            return
        try:
            idx = int(input("📖 Enter the number of the book to toggle Read/Unread: "))
            if 1 <= idx <= len(self.library):
                book = self.library[idx - 1]
                book['Read'] = not book['Read']
                status = "✔️ Read" if book['Read'] else "❌ Not Read"
                print(f"🔄 Book '{book['Title']}' is now marked as {status}.\n")
                self.save_library()
            else:
                print("\n❌ Invalid number! Please try again.\n")
        except ValueError:
            print("\n❌ Please enter a valid number (1, 2, 3, ...).\n")

    def search_book(self):
        search_title = input("\n🔍 Enter book title to search: ").lower()
        found_books = [book for book in self.library if search_title in book["Title"].lower()]
        if found_books:
            print("\n📖 Found Books:")
            for book in found_books:
                print(f"- {book['Title']} by {book['Author']} ({book['Year']})")
        else:
            print("\n🚫 No matching books found.")
        print()

    def statics(self):
        total_books = len(self.library)
        if total_books == 0:
            print("\n📭 Your library is empty.\n")
            return
        read_books = sum(1 for book in self.library if book['Read'])
        percentage = (read_books / total_books) * 100
        print(f"\n📊 Library Statistics:")
        print(f"📚 Total books: {total_books}")
        print(f"✅ Books read: {read_books}")
        print(f"📈 Read percentage: {percentage:.2f}%\n")

    def run(self):
        while True:
            print("=== 📚 Personal Library Manager ===")
            print("1. Add a book ")
            print("2. Remove a book ")
            print("3. Search for a book ")
            print("4. Display all books ")
            print("5. Display statistics ")
            print("6. Mark book as Read/Unread")
            print("7. Exit ")
            
            choice = input("👉 Enter your choice (1-7): ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()    
            elif choice == '4':
                self.view_book()
            elif choice == '5':
                self.statics()
            elif choice == '6':
                self.toggle_read_status()
            elif choice == '7':
                self.save_library()
                print("\n👋 Exiting program. Goodbye!")
                break 
            else:
                print("\n⚠️ Invalid choice, please try again.\n")

if __name__ == "__main__":
    manager = LibraryManage()
    manager.run()


