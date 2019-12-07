passwords = {}

with open("citrix.txt", "r", encoding="utf-8") as fp:
    line = fp.readline()
    while line:
        split = line.split(":")
        if len(split) < 3:
            line = fp.readline()
            continue
        password = split[2]
        if not password in passwords:
            passwords[password] = 1
        else:
            passwords[password] += 1
        line = fp.readline()

f = open("citrix_processed.txt", "w")
for password in passwords:
    f.write(password)
f.close()