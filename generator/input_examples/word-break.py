def wordBreak(s, wordDict):
  dp = [False] * (len(s) + 1)
  dp[0] = True
  
  for i in range(len(s)):
    if dp[i]:
      for j in range(i + 1, len(s) + 1):
        if s[i:j] in wordDict:
          dp[j] = True

  return dp[-1]

s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple","pen"]  
print(wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s, wordDict))
