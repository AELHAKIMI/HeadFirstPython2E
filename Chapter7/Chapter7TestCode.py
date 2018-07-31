from mysql import connector

dbconfig = {'host' : '127.0.0.1',
            'user' : 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB',
            }

conn = connector.connect(**dbconfig)
cursor = conn.cursor()

_SQL = """INSERT INTO log
                        (phrase, letters, ip, browser_string, results) 
                        VALUES
                        ('ayoub elhakimi', 'aei', '127.0.0.1','Chrome', "{'e', 'i' ,'a'}");"""
res = cursor.execute(_SQL)
conn.commit()
print(res)

_SQL = """ select * from log """
cursor.execute(_SQL)
res = cursor.fetchall()
for row in res:
    print(row)

# CREATE TABLE log (
#   id int(11) NOT NULL AUTO_INCREMENT,
#   ts timestamp NULL DEFAULT CURRENT_TIMESTAMP,
#   phrase varchar(128) NOT NULL,
#   letters varchar(128) NOT NULL,
#   ip varchar(16) NOT NULL,
#   browser_string varchar(256) not null,
#   results varchar(64) NOT NULL,
#   PRIMARY KEY (`id`)
# );


