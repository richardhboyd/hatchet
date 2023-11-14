def isHappy(n):
  past = set()
  
  while n != 1:
    n = sum(int(i)**2 for i in str(n))
    if n in past:
      return False
    past.add(n)
    
  return True

print(isHappy(19)) # True
print(isHappy(2)) # False
