def partition(s):
    result = []
    part = []
    
    def is_palindrome(s):
        return s == s[::-1]
    
    def backtrack(i):
        if i >= len(s):
            result.append(part[:])
            return
        
        for j in range(i, len(s)):
            if is_palindrome(s[i:j+1]):
                part.append(s[i:j+1])
                backtrack(j+1)
                part.pop()
        
    backtrack(0)
    return result

s = "aab"
print(partition(s))

s = "a" 
print(partition(s))
