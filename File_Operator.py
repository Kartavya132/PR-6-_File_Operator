import os
import datetime
from sys import exit

ENTRY_DATA = "data.txt"
data = []


class Entry:
    def __init__(self):
        pass

    def adding_entry(self):
        print("\n-------------------------")
        print("Enter your diary entry below:")
        d_entry = input().strip()

        if not d_entry:
            print("Entry cannot be empty!")
            return

        date_today = datetime.date.today()

        data.append([str(date_today), d_entry])

        try:
            with open(ENTRY_DATA, "a") as f:
                f.write(f"{date_today}\n")
                f.write(f"{d_entry}\n")

            print("The entry was successfully added.")

        except PermissionError:
            print("Unable to save the entry due to file permission issues.")

    def view_entry(self):
        print("\n-------------------------")

        if not data:
            print("There are no diary entries.")
            return

        for index, item in enumerate(data, start=1):
            print(f"{index}.")
            print(f"   Date : {item[0]}")
            print(f"   Entry: {item[1]}")
            print()

    def check_entry(self):
        print("\n-------------------------")

        if not data:
            print("There are no diary entries.")
            return

        search_text = input("Enter text to search: ").strip()

        if len(search_text) < 3:
            print("Please enter at least 3 characters.")
            return

        found = False

        for index, item in enumerate(data, start=1):
            if search_text.lower() in item[1].lower():
                print(f"\n{index}.")
                print(f"   Date : {item[0]}")
                print(f"   Entry: {item[1]}")
                found = True

        if not found:
            print("No matching entry found.")

    def del_entry(self):
        global data

        print("\n-------------------------")

        if not data:
            print("There are no entries to delete.")
            return

        confirm = input(
            "Are you sure you want to delete all entries? (y/n): "
        ).strip().lower()

        if confirm == "y":
            data.clear()

            try:
                with open(ENTRY_DATA, "w"):
                    pass

                print("All diary entries have been deleted.")

            except PermissionError:
                print("Unable to clear the file.")
        else:
            print("Deletion cancelled.")


def load_data():
    global data
    data = []

    if not os.path.exists(ENTRY_DATA):
        with open(ENTRY_DATA, "w"):
            pass
        return

    try:
        with open(ENTRY_DATA, "r") as f:
            lines = [line.strip() for line in f.readlines()]

        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                date = lines[i]
                entry = lines[i + 1]
                data.append([date, entry])

    except (PermissionError, FileNotFoundError):
        print("Could not load diary data.")


def show():
    print("\n-----------------------------------")
    print("| Welcome to Personal Diary Entry |")
    print("-----------------------------------")
    print("1. Add a new Entry")
    print("2. View all Entries")
    print("3. Search an Entry")
    print("4. Delete all Entries")
    print("5. Exit")

    return input("Enter your choice: ").strip()


def main():
    load_data()

    diary = Entry()

    while True:
        choice = show()

        match choice:
            case "1":
                diary.adding_entry()

            case "2":
                diary.view_entry()

            case "3":
                diary.check_entry()

            case "4":
                diary.del_entry()

            case "5":
                print("Thank you for using Personal Diary.")
                exit()

            case _:
                print("Please enter a valid choice (1-5).")


if __name__ == "__main__":
    main()
