# Create a dictionary to store employee data
emp_dict = {} 

# Loop through the employee table
for emp in Employee:
  emp_id = emp[0]
  emp_name = emp[1]
  emp_salary = emp[2]
  emp_manager_id = emp[3]
  
  # Store employee data in dictionary
  emp_dict[emp_id] = [emp_name, emp_salary, emp_manager_id]

# Initialize result list  
result = []

# Loop through all employees
for emp_id, emp_data in emp_dict.items():
  
  # Get manager id
  manager_id = emp_data[2]  
  
  # Check if manager exists
  if manager_id in emp_dict:
   
    # Get manager salary  
    manager_salary = emp_dict[manager_id][1]
    
    # Check if employee earns more than manager
    if emp_data[1] > manager_salary:
      result.append([emp_data[0]])
      
# Return result      
print(result)
