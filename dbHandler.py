import sqlite3



class dbHandler:
    def __init__(self):
        self.con = sqlite3.connect("analysis.db")

        try:
            self.con.execute("CREATE TABLE data (ip TEXT NOT NULL, logitude BLOB NOT NULL, latitude BLOB NOT NULL)")
        except:
            pass

    def add(self, ip, logitude, latitude):
        query = """INSERT INTO data (ip, logitude, latitude) VALUES (?,?,?)"""
        self.con.execute(query, (ip, logitude, latitude))
        self.con.commit()
        