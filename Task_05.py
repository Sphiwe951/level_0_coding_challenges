import math

def tri_area(len1, len2, len3):
    s = 0.5*(len1+len2+len3)
    val = s*((s-len1)*(s-len2)*(s-len3))
    return math.sqrt(val)
    