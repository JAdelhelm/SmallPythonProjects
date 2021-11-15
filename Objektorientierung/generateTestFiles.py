import random as r
with open("testfile.txt","w+") as w:
    for i in range(0,100):
        for j in range(0,20):
            w.write(str(r.randint(0,40))+" ")
        w.write("\n")
