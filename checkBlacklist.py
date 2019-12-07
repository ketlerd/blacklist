import sys
import hashlib
import os

notFound = []
found = []
files = []
avg = 0
shortest = 16
longest = 0

for r, d, f in os.walk("/mnt/f/hashed/"):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

def search(fptr,value, low, high):
    if(low > high):
        return 0
    mid = (low+high) // 2

    fptr.seek(mid*41, 0) #byte align to sha1 length :(
    line = fptr.readline().rstrip('\r\n')

    if(value < line):
        return search(fptr, value, low, mid-1)
    
    elif(value > line):
        return search(fptr, value, mid+1, high)
    else:
        return 1

def searchSpecificPassword(password):
    for f in files:
        with open(f, 'rb') as fptr:
            password = password.rstrip('\r\n')
            result = search(fptr, hashlib.sha1(password).hexdigest().upper(), 0, (os.path.getsize(f)/41) - 1)
            if result == 0:
                if password not in notFound:
                    notFound.append(password)
            else:
                try:
                    found.append(password)
                except:
                    pass

def searchFiles():
    with open(sys.argv[1], 'r') as inFile:
        for p in inFile:
            password = p.rstrip('\r\n')
            cont = False
            
            for f in files:    
                if cont:
                    break
                with open(f, 'rb') as fptr:
                    result = search(fptr, hashlib.sha1(password).hexdigest().upper(), 0, (os.path.getsize(f)/41) - 1)
                    if result == 0:
                        if password not in notFound:
                            notFound.append(password)
                    else:
                        try:
                            found.append(password)
                            cont = True
                        except:
                            pass                            

if sys.argv[1] == "-l":
    for f in files:
        print(f)
    exit()
elif ".txt" in sys.argv[1]:
    count = 0
    #find the number of leaked passwords
    with open(sys.argv[1], 'r') as f:
        for l in f:
            length = len(l)
            count = count + 1
            avg = avg + length
            if length < shortest:
                shortest = length
            if length > longest:
                longest = length
    searchFiles()
else:
    searchSpecificPassword(sys.argv[1])

for f in found:
    try:
        notFound.remove(f)
    except:
        pass

print("+-------------------------------------+")
print("|  PASSWORDS NOT CONTAINED IN LISTS   |")
print("+-------------------------------------+")
if ".txt" in sys.argv[1]:
    print("        " + sys.argv[1] + "\n")
for p in notFound:
    print(p)

if ".txt" in sys.argv[1]:
    print("\n")
    print("total: " + str(count) + ",    !blacklisted: " + str(len(notFound)) + ",  %: " + str(len(notFound)/float(count)))
    print("average length: " + str(avg/count) + "   shortest: " + str(shortest) + "    longest: " + str(longest))    
