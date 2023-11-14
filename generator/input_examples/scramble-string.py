import random

def isScramble(s1, s2):
    if len(s1) != len(s2):
        return False
    
    if s1 == s2:
        return True
    
    if sorted(s1) != sorted(s2):
        return False

    for i in range(1, len(s1)):
        s1_left = s1[:i]
        s1_right = s1[i:]
        s2_left = s2[:i] 
        s2_right = s2[i:]

        if (isScramble(s1_left, s2_left) and isScramble(s1_right, s2_right)) or \
           (isScramble(s1_left, s2_right) and isScramble(s1_right, s2_left)):
            return True
    
    return False
        
print(isScramble("great", "rgeat")) # True
print(isScramble("abcde", "caebd")) # False
print(isScramble("a", "a")) # True
