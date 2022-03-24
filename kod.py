with open('after-z.txt')as f:
    lines = f.readlines()

szamok = "0123456789"
osszeg = 0
db = 0



for line in lines:
    for i, betu in enumerate(line):
        if betu == 'Z' and line[i + 1] in szamok:
            osszeg += int(line[i + 1])
            db += 1

atlag = osszeg // db

print(atlag)

            

