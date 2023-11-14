def generate_expressions(num, target):
    if not num:
        return []
    
    result = []
    for i in range(1, len(num)):
        left = num[:i]
        right = num[i:]
        
        left_expressions = generate_expressions(left, target)
        right_expressions = generate_expressions(right, target)
        
        for l in left_expressions:
            for r in right_expressions:
                result.append(l + "*" + r)
                result.append(l + "+" + r)
                result.append(l + "-" + r)
                
    if num[0] != '0': 
        result.append(num)
        
    return [r for r in result if eval(r) == target]
