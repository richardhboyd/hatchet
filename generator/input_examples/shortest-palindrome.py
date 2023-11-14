def shortest_palindrome(s):
    rev = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(rev[i:]):
            return rev[:i] + s
    return ""

s = "aacecaaa"
print(shortest_palindrome(s))

s = "abcd"  
print(shortest_palindrome(s))
