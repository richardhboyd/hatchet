def getHint(secret, guess):
    bulls = sum(s==g for s,g in zip(secret, guess))
    
    secret_digits = [0] * 10
    guess_digits = [0] * 10
    for s in secret:
        secret_digits[int(s)] += 1
    for g in guess:
        guess_digits[int(g)] += 1
        
    cows = sum(min(secret_digits[i], guess_digits[i]) for i in range(10)) - bulls
        
    return f'{bulls}A{cows}B'


secret = "1807"
guess = "7810"
print(getHint(secret, guess)) 

# Output: 1A3B
