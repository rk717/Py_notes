XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

-------------------------------------------------------------------------
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

--------------------------------------------------------------------------
def xo(s):

  exes = 0
  ohs = 0

  for c in s.lower():
    if c == 'x':
      exes += 1
    elif c == 'o':
      ohs += 1

  return exes == ohs
 
 
 
 ----------------------------------------------------------------------------
 from collections import Counter

def xo(s):
    d = Counter(s.lower())
    return d.get('x', 0) == d.get('o', 0)
