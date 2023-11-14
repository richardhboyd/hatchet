def isIsomorphic(s, t):
  if len(s) != len(t):
    return False

  char_map = {}
  used_chars = set()

  for i, char in enumerate(s):
    if char not in char_map:
      if t[i] in used_chars:
        return False
      char_map[char] = t[i]
      used_chars.add(t[i])
    elif char_map[char] != t[i]:
      return False

  return True
