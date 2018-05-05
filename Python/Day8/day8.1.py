import re

f = open('Day8Text.txt', 'r')
tuples = re.findall(r'(\S+)\s(\S+)\s(-?\w+)\sif\s(\w+)\s(.+)', f.read())

valdict = {}
for tuple in tuples:
    if tuple[0] not in valdict.keys():
        valdict[tuple[0]]=0

for tuple in tuples:
    temp = 'valdict[tuple[3]] ' + tuple[4]
    if eval(temp) == True:
        add = tuple[2]
        addthis = eval(add)
        if tuple[1] == 'inc':
            valdict[tuple[0]] += addthis
        else:
            valdict[tuple[0]] -= addthis

m = []
for val in sorted(valdict.values(), reverse=True):
    m.append(val)
for k, v in valdict.items():
    if v == m[0]:
        print(k, v)