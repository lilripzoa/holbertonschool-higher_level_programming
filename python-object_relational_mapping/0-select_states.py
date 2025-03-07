#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """connect database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    state = cursor.fetchall()

    for row in state:
        print(row)

    cursor.close()
    db.close()