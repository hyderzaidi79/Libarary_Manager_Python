# 📚 Personal Library Manager (Python CLI App)

A simple and interactive command-line application for managing your personal book library. Built in Python, this tool allows you to add, remove, view, search, and track your reading progress — all stored in a local `.txt` file using JSON format.

---

## ✨ Features

- ➕ Add a new book with title, author, year, and read status
- 🗑️ Remove books by index
- 🔍 Search books by title
- 📖 Mark books as read or unread
- 📋 View your complete library
- 📊 See statistics like total books and read percentage
- 💾 Persistent storage using a local `library.txt` file

---

## 🛠 Requirements

- Python 3.x

No external libraries are required, as it uses only the built-in `json` module.

---

## 🚀 Getting Started

1. **Clone or download this repository.**

2. **Run the application:**
```bash
python library_manager.py

🧑‍💻 How to Use

Once you run the script, you will see a menu:

=== 📚 Personal Library Manager ===
1. Add a book 
2. Remove a book 
3. Search for a book 
4. Display all books 
5. Display statistics 
6. Mark book as Read/Unread
7. Exit 

Choose an option by entering a number (e.g., 1 to add a book).

Books are saved automatically in library.txt.
💾 File Structure

    library.txt: JSON file to store book data persistently

    library_manager.py: Main Python script containing the logic

📄 Example

📚 Enter book title: Atomic Habits
✍️ Enter author: James Clear
📅 Enter publication year: 2018
✅ Have you read this book? (y/n): y
✅ Book 'Atomic Habits' added to your library!

📊 Library Statistics:
📚 Total books: 5
✅ Books read: 3
📈 Read percentage: 60.00%

📌 Possible Enhancements

    Export/Import to CSV

    GUI version with Tkinter or PyQt

    Tagging or genre-based organization

    Sync with cloud storage or Google Books API

📄 License

This project is licensed under the MIT License.
🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.


Would you like help creating a logo, turning it into a `.exe` file, or setting it up as a desktop app?

