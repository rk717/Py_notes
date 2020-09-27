Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

def make_readable(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"  #return "%02d:%02d:%02d" % (h, m, s)
print(make_readable(359999))

def make_readable(seconds):
    hours = seconds/3600
    min = (seconds%3600)/60
    sec = seconds%60
    return "{:02d}:{:02d}:{:02d}".format(hours,min,sec)
