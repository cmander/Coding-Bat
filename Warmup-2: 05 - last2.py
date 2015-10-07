# CODING BAT > Warmup-2 > last2

def last2(string):
    if len(string) <= 2:
        return 0

    last2 = string[len(string) - 2:] # stores the last two chars from string
    count = 0

    for i in range(len(string) - 2): # loop through string ignoring last two chars
        sub = string[i:i+2] # first iteration will be first and second char, second iteration will be second and third char, and so on...
        if sub == last2:
            count += 1
    return count
