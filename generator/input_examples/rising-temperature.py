import sqlite3

conn = sqlite3.connect('weather.db')
c = conn.cursor()

c.execute('''
          SELECT id
          FROM Weather w1
          WHERE EXISTS (SELECT 1 
                        FROM Weather w2
                        WHERE w2.recordDate = date(w1.recordDate, '-1 day')
                        AND w1.temperature > w2.temperature)
          ''')

result = c.fetchall()

print('Ids with higher temperature than previous day:')
for id in result:
    print(id[0])

conn.close()
