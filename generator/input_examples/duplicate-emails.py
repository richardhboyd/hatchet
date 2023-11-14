from collections import defaultdict

class Person:
    def __init__(self, id, email):
        self.id = id
        self.email = email

person_table = [
  Person(1, "a@b.com"),
  Person(2, "c@d.com"),
  Person(3, "a@b.com")  
]

email_counts = defaultdict(int)

for person in person_table:
    email_counts[person.email] += 1
    
duplicate_emails = []
for email, count in email_counts.items():
    if count > 1:
        duplicate_emails.append(email)
        
print(duplicate_emails)
