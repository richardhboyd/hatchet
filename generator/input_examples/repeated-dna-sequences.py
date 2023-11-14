def find_repeats(s):
    repeats = []
    for i in range(len(s)-10+1):
        sub = s[i:i+10]
        if sub in s[i+1:] and sub not in repeats:
            repeats.append(sub)
    return repeats

dna = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" 

print(find_repeats(dna))
