#!/usr/bin/python3
"""
Lists all cities of a given state from the database `hbtn_0e_4_usa`
in ascending order.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Accesses the database
    Return: all cities filtered by state in hbtn_0e_0_usa
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306, user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM cities JOIN states \
                ON cities.state_id = states.id ORDER BY cities.id")
    [print(", ".join([c[2] for c in cur.fetchall() if c[4] == sys.argv[4]]))]
