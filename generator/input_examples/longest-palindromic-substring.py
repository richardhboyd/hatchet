def longestPalindrome(s):
    max_len = 0
    start = 0
    end = 0
    
    for i in range(len(s)):
        # Odd length palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                end = r
                max_len = r - l + 1
            l -= 1
            r += 1
            
        # Even length palindromes
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                end = r
                max_len = r - l + 1
            l -= 1
            r += 1
    
    return s[start:end+1]
