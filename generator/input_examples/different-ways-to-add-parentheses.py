from itertools import product

def diffWaysToCompute(expression):
    if expression.isdigit():
        return [int(expression)]
    
    results = []
    for i, char in enumerate(expression):
        if char in '+-*':
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i+1:])
            for l in left:
                for r in right:
                    if char == '+':
                        results.append(l + r)
                    elif char == '-':
                        results.append(l - r)
                    else:
                        results.append(l * r)
    
    return results

expression1 = "2-1-1"
print(diffWaysToCompute(expression1)) # [0, 2]

expression2 = "2*3-4*5"  
print(diffWaysToCompute(expression2)) # [-34, -14, -10, -10, 10]
