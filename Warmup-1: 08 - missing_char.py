# CODING BAT > Warmup-1 > missing_char

def missing_char(string, n):
    new_string = ""
    if n > len(string) - 1:
        return False
    else:
        for i in range(len(string)):
            if i == n:
                continue
            else:
                new_string = new_string + string[i]
    return new_string
