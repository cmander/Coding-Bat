# CODING BAT > Warmup-2 > front_times

def front_times(string, n):
    new_string = ""
    if len(string) < 3:
        for i in range(len(string)):
            new_string = new_string + string[i]
    else:
        for i in range(3):
            new_string = new_string + string[i]
    return new_string * n
