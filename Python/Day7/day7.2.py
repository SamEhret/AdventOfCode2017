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
        dictionary[tuple[0]] = None

dictvalue = dictionary.values()
listvalue = re.findall(r'\w+', str(dictvalue))

x = 1
newlist = []
templist = []
for key in dictionary:
    if key not in listvalue:
        for val in dictionary[key]:
            newlist.append((key, val, x))
            x = x + 1
        templist.append(key)
for val in templist:
    del dictionary[val]
templist = []

while len(dictionary.keys()):
    for val in newlist:
        if val[1] != None:
            print(val)
            for key in dictionary.keys():
                if val[1] == key:
                    if dictionary[key] != None:
                        for value in dictionary[key]:
                            #print((val[1], value.strip(), x))
                            newlist.append((val[1], value.strip(), x))
                            x = x + 1
                        del dictionary[key]
                        break
                    else:
                        #print((val[1], None, x))
                        newlist.append((val[1], None, x))
                        x = x + 1
                    del dictionary[key]
                    break

#print(newlist)
#print(len(dictionary.keys()))

#children = {}
#objs = []
#l = []
#for parent, child, id in newlist:
#    obj = {
#        'id': id,
#        'parent': parent,
#        'child': child
#    }
#    objs.append(obj)

#    if parent == root[0]:
#        l.append(obj)
    
#    elif parent not in children:
#        children[parent] = []
#    children[parent].append(obj)

#for obj in objs:
#    if obj['id'] in children:
#        obj['son'] = children[obj['id']]