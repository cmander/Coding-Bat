# CODING BAT > Warumup-2 > string_match

def string_match(a, b):
    if len(a) > len(b): # or use the 'min' function
        c = a
    else:
        c = b

    count = 0
    
    for i in range(len(c) - 1):
        sub_a = a[i:i + 2]
        sub_b = b[i:i + 2]
        
        if sub_a == sub_b:
            count += 1

    return count
