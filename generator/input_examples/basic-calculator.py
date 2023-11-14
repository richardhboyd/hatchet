def calculate(s):
    stack = []
    current_num = 0
    operation = None
    
    for c in s:
        if c.isdigit():
            current_num = current_num*10 + int(c)
        elif c in '+-':
            if operation:
                if operation == '+':
                    stack.append(current_num) 
                else:
                    stack.append(-current_num)
            current_num = 0
            operation = c
        elif c == '(':
            stack.append(current_num)
            current_num = 0
            operation = None
        elif c == ')':
            if operation == '+':
                stack.append(current_num)
            else:
                stack.append(-current_num)
            current_num = sum(stack)
            stack = []
            operation = None
            
    if operation == '+':
        stack.append(current_num)
    else:
        stack.append(-current_num)
        
    return sum(stack)
