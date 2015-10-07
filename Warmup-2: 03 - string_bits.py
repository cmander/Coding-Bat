# CODING BAT > Warmup-2 > string_bits

def string_bits(string):
    new_string = ""
    for i in range(0, len(string), 2):
        new_string = new_string + string[i]
    return new_string
