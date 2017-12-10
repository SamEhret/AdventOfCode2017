import sys

jumplist = []
f = open('Day5List.txt', 'r')
for line in f:
    line = line.strip()
    jumplist.append(int(line))

x = 0
count = 0
y = jumplist[x]
while jumplist:
    if y >= 3:
        jumplist[x] = y - 1
        x = x + y
        count = count + 1
        if x < 0 or x >= len(jumplist):
            print(count)
            sys.exit()
        y = jumplist[x]
    else:
        jumplist[x] = y + 1
        x = x + y
        count = count + 1
        if x < 0 or x >= len(jumplist):
            print(count)
            sys.exit()
        y = jumplist[x]