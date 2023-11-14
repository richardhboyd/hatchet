import pandas as pd

# Create sample data
data = {'id': [1,2,3,4,5,6], 
        'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]}
scores = pd.DataFrame(data)

# Rank the scores
scores['rank'] = scores['score'].rank(method='dense', ascending=False)

# Output result 
print(scores.sort_values('score', ascending=False)[['score','rank']])
