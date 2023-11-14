def titleToNumber(columnTitle):
    result = 0
    for c in columnTitle:
        result *= 26
        result += ord(c) - ord('A') + 1
    return result

print(titleToNumber("A")) # 1
print(titleToNumber("AB")) # 28  
print(titleToNumber("ZY")) # 701
