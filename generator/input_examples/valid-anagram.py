def isAnagram(s, t):
  # Convert strings to lowercase and remove whitespace
  s = s.lower().replace(' ', '') 
  t = t.lower().replace(' ', '')

  # Check if lengths are different
  if len(s) != len(t):
    return False

  # Count frequency of each character
  count = {}
  for char in s:
    if char in count:
      count[char] += 1
    else:
      count[char] = 1
  
  # Check if frequencies match
  for char in t:
    if char in count:
      count[char] -= 1
    else:
      return False
  
  return all(value == 0 for value in count.values())


def isAnagramUnicode(s, t):
  return sorted(s.lower()) == sorted(t.lower())
