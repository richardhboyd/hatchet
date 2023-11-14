class NestedIterator:
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]
        
    def next(self) -> int:
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
            
    def hasNext(self) -> bool:
        while self.stack:
            nestedList, i = self.stack[-1]
            if i == len(nestedList):
                self.stack.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                self.stack[-1][1] += 1
                self.stack.append([x.getList(), 0])
        return False
