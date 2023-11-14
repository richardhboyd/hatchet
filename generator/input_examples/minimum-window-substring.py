def minWindow(s, t):
    if len(t) > len(s):
        return ""
    
    countT = {}
    for c in t:
        countT[c] = 1 if c not in countT else countT[c] + 1
    
    have = 0
    need = len(countT)
    
    res = ""
    resLen = float("infinity")
    
    l = 0
    for r in range(len(s)):
        c = s[r]
        if c in countT:
            countT[c] -= 1
            if countT[c] == 0:
                have += 1
                
        while have == need:
            if (r - l + 1) < resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            
            if s[l] in countT:
                countT[s[l]] += 1
                if countT[s[l]] == 1:
                    have -= 1
            l += 1
        
    return res
