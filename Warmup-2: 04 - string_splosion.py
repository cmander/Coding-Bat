# CODING BAT > Warmup-2 > string_splosion

def string_splosion(string):
    new_string = ""
    for i in range(len(string) + 1):
        new_string = new_string + string[:i]

    return new_string
