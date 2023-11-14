def getRow(rowIndex):
    row = [1]
    for i in range(1, rowIndex+1):
        prev = row
        row = [1]
        for j in range(1, i):
            row.append(prev[j-1] + prev[j])
        row.append(1)
    return row
