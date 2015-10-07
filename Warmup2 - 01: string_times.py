# CODING BAT > Warmup-2 > string_times

def string_times(string, n):
    new_string = ""
    if n < 0:
        return False
    else:
        for i in range(n):
            new_string = new_string + string
    return new_string
