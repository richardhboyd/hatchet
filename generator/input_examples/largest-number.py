from functools import cmp_to_key

def largestNumber(nums):
    
    # Convert nums to strings
    nums = [str(num) for num in nums]
    
    # Define custom comparison function that sorts in descending order
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0
        
    # Sort nums using custom comparison    
    nums.sort(key=cmp_to_key(compare))
    
    # Join sorted nums into string 
    return ''.join(nums)

nums = [10, 2] 
print(largestNumber(nums)) # 210

nums = [3, 30, 34, 5, 9]
print(largestNumber(nums)) # 9534330
