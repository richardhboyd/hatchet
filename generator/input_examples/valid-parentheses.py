def is_valid(s):
  stack = []

  for char in s:
    if char in ['(', '{', '[']:
      stack.append(char)
    elif char == ')':
      if not stack or stack[-1] != '(':
        return False
      stack.pop() 
    elif char == '}':
      if not stack or stack[-1] != '{': 
        return False
      stack.pop()
    elif char == ']':  
      if not stack or stack[-1] != '[':
        return False
      stack.pop()

  return not stack

print(is_valid("()")) # True
print(is_valid("()[]{}")) # True 
print(is_valid("(]")) # False
