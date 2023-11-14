def find_concatenated_substring(s, words):
    n = len(words)
    word_len = len(words[0])
    sub_len = n * word_len
    
    result = []
    for i in range(len(s) - sub_len + 1):
        sub = s[i:i+sub_len]
        seen = [False] * n
        for j in range(0, sub_len, word_len):
            word = sub[j:j+word_len]
            if word not in words:
                break
            seen[words.index(word)] = True
        if all(seen):
            result.append(i)
            
    return result
