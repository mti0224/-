import time, random
f = open("money.txt","r")
num = f.readline()
print(num)
f.close()
while True:
    time.sleep(1)
    g = open("money.txt","w")
    plus = random.randint(1,10)
    g.write(str(int(num)+plus))
    g.close()
    f = open("money.txt","r")
    num = f.readline()
    print(num)
    f.close()
    
