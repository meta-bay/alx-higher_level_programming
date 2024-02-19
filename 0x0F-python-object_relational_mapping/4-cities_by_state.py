#!/usr/bin/python3
'''
    cities
'''


if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute('SELECT cities.id, cities.name, states.name \
            FROM cities, states WHERE cities.state_id = states.id')
    cities = curs.fetchall()
    for city in cities:
        print(city)
    curs.close()
    db.close()
