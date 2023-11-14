def isUgly(num):
    if num <= 0:
        return False
    
    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    
    return num == 1

num = 14
print(isUgly(num)) # False

num = 6 
print(isUgly(num)) # True
