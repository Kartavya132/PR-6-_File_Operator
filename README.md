# 📖 Personal Diary Entry Application

A simple yet practical **Personal Diary Entry Application** built using **Python**. This command-line project allows users to maintain a personal diary by adding entries, viewing saved memories, searching through previous notes, and deleting all stored entries when necessary.

Whether you want to keep track of your daily activities, record important moments, or simply practice Python file handling and object-oriented programming, this project provides an easy-to-understand solution.

---

# ✨ Features

✅ Add new diary entries with the current date

✅ View all saved diary entries

✅ Search for entries using keywords or phrases

✅ Delete all diary records when required

✅ Store data permanently in a text file

✅ Automatically load existing entries on startup

✅ Beginner-friendly Python project

---

# 🎯 Project Objectives

This project demonstrates the use of:

* 📂 File Handling
* 🏗️ Object-Oriented Programming (OOP)
* 🔄 Loops and Conditional Statements
* 📝 User Input Handling
* ⚠️ Basic Exception Handling
* 📅 Date Management

---

# 📁 Project Structure

```text
Personal-Diary/
│
├── diary.py        # Main Python program
├── data.txt        # Stores diary entries
└── README.md       # Project documentation
```

---

# 🧠 How It Works

The application stores diary entries in a local text file named `data.txt`.

Each diary entry contains:

1. 📅 Date of entry
2. 📝 User's diary content

When the application starts:

* It checks whether `data.txt` exists.
* Existing entries are loaded into memory.
* Users can perform various operations through the menu system.

---

# 🖥️ Main Menu

When the application launches, users are greeted with the following interface:

```text
-----------------------------------
| Welcome to Personal Diary Entry |
-----------------------------------

-------Entry Menu-------
1. Add the new Entry
2. View all Entry
3. Search for an Entry
4. Delete all the Entries
5. Exit
```

---

# ➕ Adding a New Diary Entry

Selecting option **1** allows users to create a new diary entry.

### Example

```text
Enter the choice : 1

-------------------------
Enter your diary entry below

Today I completed my Python diary project.

The Entry is Successfully Added
```

The entry is automatically stored in the `data.txt` file.

---

# 📚 Viewing All Entries

Selecting option **2** displays all stored diary records.

### Example

```text
Enter the choice : 2

------------------------

1.
  2026-06-18
  Today I completed my Python diary project.

2.
  2026-06-19
  Learned about file handling and exceptions.
```

This feature helps users review their past records quickly.

---

# 🔍 Searching for an Entry

Selecting option **3** allows users to search through saved entries using keywords.

### Example

```text
Enter the choice : 3

----------------------
Enter the diary entry to check below :

Python
```

### Output

```text
1.
  2026-06-18
  Today I completed my Python diary project.
```

---

# ❌ Search Result Not Found

If no matching entry exists:

```text
Enter the choice : 3

----------------------
Enter the diary entry to check below :

Vacation

There is no such thing!!
```

---

# 🗑️ Deleting All Entries

Selecting option **4** removes all stored diary records.

### Example

```text
Enter the choice : 4

----------------------

The data completely removed!
```

After deletion, the diary becomes empty.

---

# 🚪 Exiting the Application

Selecting option **5** closes the application safely.

### Example

```text
Enter the choice : 5

Thank you for this!
```

---

# 💾 Data Storage Format

All diary entries are stored inside `data.txt`.

### Example File Content

```text
2026-06-18
Today I completed my Python diary project.

2026-06-19
Learned about file handling and exceptions.

2026-06-20
Started learning object-oriented programming.
```

This ensures entries remain available even after the program is closed.

---

# 📸 Complete Demonstration

```text
-----------------------------------
| Welcome to Personal Diary Entry |
-----------------------------------

-------Entry Menu-------
1. Add the new Entry
2. View all Entry
3. Search for an Entry
4. Delete all the Entries
5. Exit

Enter the choice : 1

-------------------------
Enter your diary entry below

Today was a productive day.

The Entry is Successfully Added

Enter the choice : 2

------------------------

1.
  2026-06-18
  Today was a productive day.

Enter the choice : 3

----------------------
Enter the diary entry to check below :

productive

1.
  2026-06-18
  Today was a productive day.

Enter the choice : 5

Thank you for this!
```

---

# 🛠️ Technologies Used

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| 🐍 Python             | Core Programming Language |
| 📂 File Handling      | Data Storage              |
| 🏗️ OOP               | Application Structure     |
| ⚠️ Exception Handling | Error Management          |
| 📅 Datetime Module    | Date Management           |

---

# 🎓 Learning Outcomes

After studying this project, learners can understand:

* Creating classes and methods in Python
* Reading and writing files
* Managing application data
* Working with lists
* Handling exceptions
* Building menu-driven programs
* Implementing simple CRUD operations

---

