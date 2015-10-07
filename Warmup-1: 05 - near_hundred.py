# CODING BAT > Warmup-1 > near_hundred

def near_hundred(n):
    if n >= 100 - 10 or n <= 100 + 10:
        return True
    elif n >= 200 - 10 or n <= 200 + 10:
        return True
    else:
        return False
