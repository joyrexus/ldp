from collections import defaultdict as dd

def autodict(): return dd(autodict)
d = autodict()
d['an']['arbitrarily']['deep']['dictionary'] = "yes!"
