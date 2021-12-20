import math
from collections import Counter

def eta(probs):
    base = 2
    
    ent = 0
    for p in probs:
        if p > 0.:
            ent -= float(p) * math.log(p, base)

    return ent
