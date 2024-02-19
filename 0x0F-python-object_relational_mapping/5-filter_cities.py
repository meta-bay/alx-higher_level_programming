#!/usr/bin/python3
'''
    cities in the state
'''


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    sql = '''SELECT cites.name FROM cities 
    INNER JOIN states ON cities.state_id = states.id 
    WHERE states.name = %s ORDER BY cites.id ASC'''
    curs.execute(sql, (sys.argv[4],))
    cities = curs.fetchall()
    city_in_s = ", ".join(city[0] for city in cities)
    print(city_in_s)
    curs.close()
    db.close()
