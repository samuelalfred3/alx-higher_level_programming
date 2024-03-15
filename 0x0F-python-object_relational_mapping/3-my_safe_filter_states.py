#!/usr/bin/python3
import sys
import MySQLdb

"""
Script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. This script is safe from MySQL injections.
"""

"""
Function to filter states by name
"""
def filter_states(username, password, database, state_name):
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
    """
    Use parameterized query to prevent SQL injection
    """
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    """
    Print the fetched results
    """
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        exit(1)
    username, password, database, state_name = sys.argv[1:]
    filter_states(username, password, database, state_name)

