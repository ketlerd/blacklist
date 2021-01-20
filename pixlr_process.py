import json

passwords = {}

with open("pixlr.json", "r", encoding="utf-8") as fp:
    line = fp.readline()
    while line:
        l = json.loads(line)

        if('password' in l):
            password = l["password"]
        
        if not password in passwords:
            passwords[password] = 1
        else:
            passwords[password] += 1
        line = fp.readline()

f = open("pixlr_processed.txt", "w")
for password in passwords:
    f.write(password + '\n')
f.close()