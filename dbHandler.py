import sqlite3



class dbHandler:
    def __init__(self):
        self.con = sqlite3.connect("analysis.db")

        try:
            self.con.execute("CREATE TABLE data")