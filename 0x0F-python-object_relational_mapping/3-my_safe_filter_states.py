#!/usr/bin/python3
'''
    safe filter states
'''


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute('SELECT * FROM states WHERE name \
            LIKE BINARY %s', sys.argv[4])
    states = curs.fetchall()
    for state in states:
        print(state)
    curs.close()
    db.close()
