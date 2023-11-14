byte_weights = [bin(i).count('1') for i in range(256)] 

def hammingWeight(n):
    weight = 0
    while n:
        weight += byte_weights[n & 0xff]
        n >>= 8
    return weight
