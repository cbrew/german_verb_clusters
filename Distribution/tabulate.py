#! /bin/env python

from string import split

import fileinput

f = {}
items = ['ahnen', 'anfangen', 'ank\xfcndigen', 'aufh\xf6ren', 'beenden', 'beginnen', 'beharren', 'bekanntgeben', 'bekommen', 'beschreiben', 'bestehen', 'blitzen', 'bringen', 'charakterisieren', 'darstellen', 'denken', 'dienen', 'donnern', 'd\xe4mmern', 'enden', 'erhalten', 'erlangen', 'er\xf6ffnen', 'essen', 'fahren', 'fliegen', 'folgen', 'freuen', 'glauben', 'helfen', 'insistieren', 'interpretieren', 'konsumieren', 'kriegen', 'lesen', 'liefern', 'liegen', 'nieseln', 'pochen', 'regnen', 'rudern', 'saufen', 'schicken', 'schlie\xdfen', 'schneien', 'segeln', 'sitzen', 'stehen', 'trinken', 'unterst\xfctzen', 'verk\xfcnden', 'vermitteln', 'vermuten', 'wissen', 'zustellen', '\xe4rgern', '\xf6ffnen']

verb = None

for line in fileinput.input():
    arr = split(line)
    if len(arr) == 1:
        verb = arr[0]
        f[verb] = {}
    elif len(arr) == 2:
        f[verb][arr[0]] = float(arr[1])

print "",
for v in f[verb].keys():
    print '"%s"' % v,
print ""
for k  in items:   # a subset of the verbs
# for k in f.keys():
    print '"%s"' % k,
    for (verb,attr) in f[k].items():
        print  attr,
    print ""


