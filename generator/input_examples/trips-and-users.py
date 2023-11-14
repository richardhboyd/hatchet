import sqlite3

conn = sqlite3.connect('rides.db')
c = conn.cursor()

c.execute('''
SELECT t.request_at AS Day,  
       round(SUM(CASE WHEN t.status LIKE 'cancelled%' AND u1.banned = 'No' AND u2.banned = 'No' THEN 1 ELSE 0 END) / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips t 
JOIN Users u1 ON t.client_id = u1.users_id
JOIN Users u2 ON t.driver_id = u2.users_id
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03' 
GROUP BY t.request_at
''')

print(c.fetchall())

conn.close()
