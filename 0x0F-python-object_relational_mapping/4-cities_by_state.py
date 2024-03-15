#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

def list_cities(username, password, database):
    """List all cities from the specified database"""
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        cur = db.cursor()

        query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC
                """
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database)

