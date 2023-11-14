def countPrimes(n):
    if n < 2:
        return 0
    
    primes = [True] * n
    primes[0] = primes[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
    
    return sum(primes)

print(countPrimes(10)) # 4
print(countPrimes(0)) # 0 
print(countPrimes(1)) # 0
