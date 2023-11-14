from collections import defaultdict, deque

def find_shortest_transformation(beginWord, endWord, wordList):
    
    if endWord not in wordList:
        return 0
    
    # Dictionary to map words to list of words that differ by 1 letter
    adj_map = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            adj_map[pattern].append(word)
            
    # BFS to find shortest path        
    queue = deque([(beginWord, 1)]) 
    visited = set()
    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            for adj_word in adj_map[pattern]:
                if adj_word not in visited:
                    visited.add(adj_word)
                    queue.append((adj_word, steps+1))
    return 0
