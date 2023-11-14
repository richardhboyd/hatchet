def sum_digits_until_single(num):
  if num == 0:
    return 0
  
  if num % 9 == 0:
    return 9
  
  return num % 9

print(sum_digits_until_single(38)) # 2 
print(sum_digits_until_single(0)) # 0
