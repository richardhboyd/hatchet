def numberToWords(num):

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    words = []
    
    if num == 0:
        return "Zero"

    i = 0
    while num > 0:
        if num % 1000 != 0:
            words.append(helper(num % 1000) + thousands[i])
        num //= 1000
        i += 1
        
    words.reverse()
    
    return " ".join(words)
    
def helper(num):
    if num == 0:
        return ""
    elif num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10] 
    elif num < 100:
        return tens[num // 10] + " " + helper(num % 10)
    else:
        return ones[num // 100] + " Hundred " + helper(num % 100) 


num = 123456789
print(numberToWords(num))

# Prints "One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine"
