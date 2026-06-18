import os
from sys import exit
from datetime import datetime

ENTRY_DATA = "PR-6-_File_Operator/data.txt"


class entry:
    def init(self):
        self.entry = None
        self.date = None


def load_data():
    global data
    data = []
    temps = []
    if os.path.exists(ENTRY_DATA):
        try:
            with open(ENTRY_DATA, "r") as f:
                for line_num, line in enumerate(f, start=1):
                    if line_num % 2 == 1:
                        temps.append(line)
                    else:
                        temps.append(line)
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
