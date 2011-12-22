# encoding: utf-8
import sys

def to_sec(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

# implementação gambi
# def to_sec(t):
#     return sum([s * (i * 60) for i, s in enumerate(map(int, t.split(':')))])
print [(t, to_sec(t)) for t in sys.argv[1:]]
