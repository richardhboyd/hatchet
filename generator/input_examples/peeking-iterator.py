class PeekingIterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self._peeked_value = None
        
    def peek(self):
        if not self.hasNext():
            return None
        if self._peeked_value is None:
            self._peeked_value = next(self._iterator)
        return self._peeked_value
    
    def next(self):
        if self._peeked_value is not None:
            result = self._peeked_value
            self._peeked_value = None
        else:
            result = next(self._iterator)
        return result
    
    def hasNext(self):
        return self._peeked_value is not None or self._iterator.hasNext()
