from DBCm import UseDatabase

dbconfig = {'host' : '127.0.0.1',
            'user' : 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogdb',
            }

with UseDatabase(dbconfig) as cursor:
    _SQL = """ SELECT * FROM log"""
    cursor.execute(_SQL)
    res = cursor.fetchall()
    for row in res:
        print(row)
