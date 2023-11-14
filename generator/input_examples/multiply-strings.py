def multiply(num1, num2):
    n1 = len(num1)
    n2 = len(num2)
    result = [0] * (n1+n2)
    
    for i in reversed(range(n1)):
        for j in reversed(range(n2)):
            multiply = int(num1[i]) * int(num2[j])
            sum = multiply + result[i+j+1]
            result[i+j] += sum // 10
            result[i+j+1] = sum % 10

    # Remove leading zeros
    i = 0
    while i < len(result) and result[i] == 0:
        i += 1
    
    result = map(str, result[i:])
    return "".join(result)

print(multiply("123", "456")) # 56088 
print(multiply("2", "3")) # 6
