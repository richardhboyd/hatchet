import re

def myAtoi(s):
    s = s.strip() 
    if not s:
        return 0
    
    sign = -1 if s[0] == '-' else 1
    if s[0] in ['-','+']:
        s = s[1:]
    s = re.findall('^[0-9]+', s)
    if not s:
        return 0
        
    try:
        res = int(''.join(s)) 
        return max(-2**31, min(sign * res, 2**31-1))
    except:
        return 2**31-1 if sign == 1 else -2**31
