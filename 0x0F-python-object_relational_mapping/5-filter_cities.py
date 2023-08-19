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
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY cities.id", (state_name,))

    cities = cur.fetchall()
    for city in cities:
        print(city[0])

    cur.close()
    db.close()
