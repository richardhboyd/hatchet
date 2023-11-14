from collections import defaultdict

# Create a dict to store customers and their order ids
customers = defaultdict(list)

# Populate customers dict
for order in Orders:
    customers[order[1]].append(order[0])
    
# Initialize result    
result = []

# Check each customer
for customer in Customers:
    if not customers[customer[0]]:
        result.append(customer[1])
        
# Print result        
print(result)
