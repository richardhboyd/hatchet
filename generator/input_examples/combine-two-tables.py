import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p 
LEFT JOIN Address a 
ON p.personId = a.personId
""")

results = c.fetchall()

for row in results:
    firstName, lastName, city, state = row
    if city is None:
        city = "Null"
    if state is None:
        state = "Null"
    print(firstName, lastName, city, state)

conn.close()
