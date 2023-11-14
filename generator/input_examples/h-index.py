def hIndex(citations):
    n = len(citations)
    citations.sort(reverse=True)
    
    for i in range(n):
        if citations[i] < i+1:
            return i
    return n

citations = [3,0,6,1,5] 
print(hIndex(citations))

citations = [1,3,1]
print(hIndex(citations))
