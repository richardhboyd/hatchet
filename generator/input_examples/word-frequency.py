import sys
from collections import Counter
print('\n'.join(f'{w} {c}' for w, c in Counter(sys.stdin.read().lower().split()).most_common()))
