import math

def triangle_area(len1, len2, len3):
    semi_perimeter = 0.5*(len1+len2+len3)
    area_value = semi_perimeter*((semi_perimeter-len1)*(semi_perimeter-len2)*(semi_perimeter-len3))
    return round(math.sqrt(area_value))