import sys

for line in sys.stdin:
    print(' '.join(word[0].upper() + word[1:] for word in line.split()))
