#!/usr/bin/python3
'''
    States with 'N'
'''


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute('SELECT * FROM states WHERE name \
                    LIKE BINARY "N%" ORDER BY id ASC')
    Nstates = curs.fetchall()
    for nstate in Nstates:
        print(nstate)
    curs.close()
    db.close()
