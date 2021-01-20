import sys
import hashlib

f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "w")
list = []

for line in f1:
    line = line.rstrip('\r\n')
    list.append(line)

print("array built, sorting")

list.sort()
