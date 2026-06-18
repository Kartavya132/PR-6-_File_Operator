import os
from sys import exit
import datetime

ENTRY_DATA = "data.txt"


class Entry:
    def init(self):
        pass

    def adding_entry(self):
        print("-------------------------")
        print("Enter your diary entry below")
        d_entry = input().strip()
        dates = datetime.date.today()
        data.append([dates, d_entry])
        try:
            with open(ENTRY_DATA, "a") as f:
                f.write(str(dates) + "\n")
                f.write(str(d_entry) + "\n")
            print("The Entry is Successfully Added")
        except FileNotFoundError or PermissionError:
            f = open(ENTRY_DATA, "w")
            print("The Data is not perfectly added please try again later!!")

    def view_entry(self):
        print("------------------------")
        if data:
            try:
                for index, items in enumerate(data, start=1):
                    print(f"{index}.\n  Date: {items[0]}\n  Entry: {items[1]}")
            except IndexError:
                print("Please delete all entry and rewrite it!")
        else:
            print("There is not a single entry!")

    def check_entry(self):
        print("----------------------")
        flag = False
        if data:
            try:
                print("Enter the diary entry to check below : ")
                check = input().strip()
                for index, item in enumerate(data, start=1):
                    if check in item[1]:
                        print(f"{index}.\n  Date: {item[0]}\n  Entry: {item[1]}")
                        flag = True
                if not flag:
                    print("There is no such thing!!")
            except IndexError:
                print("Retry this or delete all the entry!")

    def del_entry(self):
        print("----------------------")
        try:
            if data:
                data = []
                with open(ENTRY_DATA, "w") as f:
                    pass
                print("The data completely removed!")
            else:
                print("there no such data in this")
        except:
            print("Try again later")


def load_data():
    global data
    data = []
    temps = []
    if os.path.exists(ENTRY_DATA):
        try:
            with open(ENTRY_DATA, "r") as f:
                for line_num, line in enumerate(f, start=0):
                    if line_num % 2 == 0 and line:
                        temps = [line.strip()]
                    elif line and line_num % 2 == 1:
                        temps.append(line.strip())
                        data.append(temps)
                        temps = []
        except PermissionError or FileNotFoundError:
            f = open(ENTRY_DATA, "w")
    else:
        try:
            f = open(ENTRY_DATA, "x")
        except PermissionError or FileExistsError:
            f = open(ENTRY_DATA, "w")


def show():
    print("-----------------------------------")
    print("| Welcome to Personal Diary Entry |")
    print("-----------------------------------\n")

    print("-------Entry Menu-------")
    print("1. Add the new Entry")
    print("2. View all Entry")
    print("3. Search for an Entry")
    print("4. Delete all the Entries")
    print("5. Exit")

    choice = input("Enter the choice : ")

    return choice


def main():
    load_data()
    dataentry = Entry()
    while True:
        ch = show()

        match ch:

            case "1":
                dataentry.adding_entry()

            case "2":
                dataentry.view_entry()

            case "3":
                dataentry.check_entry()

            case "4":
                dataentry.del_entry()

            case "5":
                print("Thank you for this!")
                exit()


if __name__ == "__main__":
    main()
