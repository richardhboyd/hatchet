import math

def fractionToDecimal(numerator, denominator):
  result = ""
  
  # Handle negative signs
  if numerator < 0 ^ denominator < 0:
    result += "-"
  
  # Convert to integers
  numerator, denominator = abs(numerator), abs(denominator)
  
  # Append whole part
  wholePart = numerator // denominator
  result += str(wholePart)
  
  # Check for no remainder
  remainder = numerator % denominator
  if remainder == 0:
    return result
  
  # Append decimal point and fractional part 
  result += "."
  
  # Create map to store remainders as keys and position as value
  remainderMap = {}
  while remainder != 0:
    if remainder in remainderMap:
      # Repeating part - enclose in brackets
      result = result[:remainderMap[remainder]] + "(" + result[remainderMap[remainder]:] + ")"
      return result
    
    remainderMap[remainder] = len(result)
    remainder *= 10
    result += str(remainder // denominator)
    remainder %= denominator

  return result
  
