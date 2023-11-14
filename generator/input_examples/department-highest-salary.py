# Import required modules
import sqlite3

# Connect to the database 
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Query to get highest salary per department
query = """
SELECT d.name AS Department, 
       e.name AS Employee,
       e.salary AS Salary
FROM Employee e 
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN 
    (SELECT departmentId, MAX(salary) 
     FROM Employee GROUP BY departmentId)
"""

# Execute query and fetch results
cursor.execute(query)
results = cursor.fetchall()

# Print results  
print("Department", "Employee", "Salary")
for row in results:
    print(row[0], row[1], row[2])
    
# Close connection
conn.close()
