from collections import defaultdict, deque

def findSequences(beginWord, endWord, wordList):

    if endWord not in wordList:
        return []
    
    L = len(beginWord)
    
    # Dictionary to map words to adjacent words
    adj_map = defaultdict(list) 
    for word in wordList:
        for i in range(L):
            pattern = word[:i] + "*" + word[i+1:]
            adj_map[pattern].append(word)
            
    # BFS
    queue = deque([(beginWord, [beginWord])])
    min_length = float("inf")
    sequences = []
    
    while queue:
        word, seq = queue.popleft()
        
        if len(seq) > min_length:
            break
            
        if word == endWord:
            min_length = len(seq)
            sequences.append(seq)
        
        for i in range(L):
            pattern = word[:i] + "*" + word[i+1:]
            
            for adjacent in adj_map[pattern]:
                if adjacent not in seq:
                    queue.append((adjacent, seq + [adjacent]))

    return sequences
    
