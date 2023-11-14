import csv

with open('file.txt') as f:
    lines = f.read().splitlines()

rows = csv.reader(lines, delimiter=' ')
rows = list(rows)

cols = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0]))]

with open('transposed.txt', 'w') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(cols)
