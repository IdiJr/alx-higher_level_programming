#!/usr/bin/python3
"""
Lists all states from the database `hbtn_0e_0_usa`
in ascending order.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Accesses the database
    Return: all states in hbtn_0e_0_usa
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306, user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
