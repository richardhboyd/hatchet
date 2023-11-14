class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        def match(w):
            if len(word) != len(w):
                return False
            for i, c in enumerate(word):
                if c != '.' and c != w[i]:
                    return False
            return True
        
        for w in self.words:
            if match(w):
                return True
        return False
