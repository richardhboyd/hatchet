def count_ones(n):
    count = 0
    for i in range(n+1):
        num = str(i)
        count += num.count('1')
    return count
