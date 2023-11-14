import pandas as pd

# Sample data
data = {'id': [1,2,3], 
        'salary': [100, 200, 300]}
df = pd.DataFrame(data)

# Get second highest salary
second_highest = df.nlargest(2, 'salary')['salary'].iloc[1] 

# Return None if there is no second highest salary
if pd.isna(second_highest):
    print(None)
else:
    print(second_highest)
