from mysql import connector

dbconfig = {'host' : '127.0.0.1',
            'user' : 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB',
            }

conn = connector.connect(**dbconfig)
cursor = conn.cursor()

_SQL = """ describe log """
cursor.execute(_SQL)
print(cursor.fetchall())
