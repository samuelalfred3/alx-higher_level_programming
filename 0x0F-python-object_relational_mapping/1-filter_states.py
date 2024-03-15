#!/usr/bin/python3
import sys
import MySQLdb

"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

"""
Function to filter states by name starting with 'N'
"""
def filter_states(username, password, database):
    """
    Connect to MySQL database
    """
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)
    """
    Create a cursor object
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8mb4_general_ci ORDER BY id ASC")
    """
    Print the fetched results
    """
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        exit(1)
    username, password, database = sys.argv[1:]
    filter_states(username, password, database)

