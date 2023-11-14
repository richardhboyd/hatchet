def minCut(s):
  n = len(s)
  cut = [i for i in range(-1,n)]
  
  for i in range(n):
    r1, l1 = 0, i
    while l1 >= 0 and r1 < n and s[l1] == s[r1]:
      cut[r1+1] = min(cut[r1+1], cut[l1] + 1)
      l1 -= 1
      r1 += 1

    r2, l2 = i, i
    while l2 >= 0 and r2 < n and s[l2] == s[r2]:
      cut[r2+1] = min(cut[r2+1], cut[l2] + 1) 
      l2 -= 1
      r2 += 1

  return cut[n]

s = "aab"
print(minCut(s)) # 1

s = "a" 
print(minCut(s)) # 0

s = "ab"
print(minCut(s)) # 1
