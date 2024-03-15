#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

def filter_cities(username, password, database, state_name):
    """
    Filter cities by state name
    """
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        cur = db.cursor()

        query = """
                SELECT cities.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """

        cur.execute(query, (state_name,))
        cities = cur.fetchall()
        city_names = [city[0] for city in cities]
        print(", ".join(city_names))

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    filter_cities(username, password, database, state_name)

