with open('passcode.txt', 'r') as myfile:
    passphrases = myfile.readlines()
passcode = []
check = []
checksum = 0

for line in passphrases:
    passcode.append(line)
    
for val in passcode:
    line = list(val.split())
    for word in line:
        sortword = ''.join(sorted(word))
        if sortword not in check:
            check.append(sortword)
            if len(line) == len(check):
                checksum = checksum + 1
                del check[:]
                break
        else:
            del check[:]
            break

print(checksum)