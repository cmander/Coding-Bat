# CODING BAT > Warmup-1 > front_back

def front_back(string):
    new_string = string[len(string) - 1]
    for i in range(len(string) - 1):
        if i == 0:
            continue
        else:
            new_string = new_string + string[i]
    return new_string + string[0]
