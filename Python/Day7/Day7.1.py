import re

listf = []
f = open('Day7text.txt', 'r')
tuples = re.findall(r'(\w+)\s\((\d+)\)\s\-\>\s(.+)', f.read())
f.seek(0)
tuples2 = re.findall(r'(\w+)\s\((\d+)\)', f.read())

dictionary = {}
for tuple in tuples:
    dictionary[tuple[0]] = tuple[2].split(',')
for tuple in tuples2:
    if tuple[0] not in dictionary.keys():
        dictionary[tuple[0]] = ' '

dictvalue = dictionary.values()
listvalue = re.findall(r'\w+', str(dictvalue))

for key in dictionary:
    if key not in listvalue:
        print(key)