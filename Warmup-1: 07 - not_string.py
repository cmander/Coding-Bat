# CODING BAT > Warmup-1 > not_string

def not_string(string):
    if len(string) >= 3 and string[:3] == "not":
        return string
    else:
        return "not " + string  
