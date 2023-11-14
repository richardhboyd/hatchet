def word_break(s, word_dict):
    word_set = set(word_dict)
    
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    if not dp[-1]:
        return []
    
    res = []
    dfs(s, word_dict, 0, [], res)
    return res

def dfs(s, word_dict, index, path, res):
    if index == len(s):
        res.append(' '.join(path))
        return
    
    for i in range(index, len(s)):
        word = s[index:i+1]
        if word in word_dict:
            path.append(word)
            dfs(s, word_dict, i+1, path, res)
            path.pop()
