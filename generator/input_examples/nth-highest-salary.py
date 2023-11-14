import heapq

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

employees = [
    Employee(1, 100),
    Employee(2, 200),
    Employee(3, 300)
]

def getNthHighestSalary(n):
    if n > len(employees):
        return None
    
    salaries = [-emp.salary for emp in employees]
    heapq.heapify(salaries)
    
    for i in range(n-1):
        heapq.heappop(salaries)
        
    return -heapq.heappop(salaries)

print(getNthHighestSalary(2))
