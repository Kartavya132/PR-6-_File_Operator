import os
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
        with open(ENTRY_DATA, "r") as f:
            for line_num, line in enumerate(f, start=1):
                if line_num % 2 == 1:
                    temps.append(line)
                else:
                    temps.append(line)
                    data.append(temps)
                    temps = []
        return
