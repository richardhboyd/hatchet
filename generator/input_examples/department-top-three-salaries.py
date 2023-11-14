# Import modules
import sqlite3

# Connect to the database 
conn = sqlite3.connect('company.db')

# Query to get top 3 salaries per department
query = """
WITH cte AS (
  SELECT *, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rank
  FROM Employee
)
SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary 
FROM cte
JOIN Department ON cte.departmentId = Department.id
WHERE rank <= 3
ORDER BY Department, rank
"""

# Execute the query and fetch the results
cur = conn.cursor()
cur.execute(query)
result = cur.fetchall()

# Print the result 
print("{:<15} {:<10} {}".format('Department', 'Employee', 'Salary'))
for row in result:
    print("{:<15} {:<10} {}".format(row[0], row[1], row[2]))
    
# Close the connection
conn.close()
