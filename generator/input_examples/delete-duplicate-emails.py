import pandas as pd

person_df = pd.DataFrame({'id': [1, 2, 3], 
                          'email': ['john@example.com', 'bob@example.com', 'john@example.com']})

# Drop duplicate emails, keep first occurrence 
person_df.drop_duplicates(subset='email', keep='first', inplace=True)

print(person_df)
