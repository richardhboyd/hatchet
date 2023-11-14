with open('file.txt') as f:
    lines = f.readlines()
    if len(lines) >= 10:
        print(lines[9])
