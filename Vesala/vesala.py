import random

BROJ_ZIVOTA = 6
DATOTEKA = open("Reci.txt","r")
RECI = DATOTEKA.readlines()
print(RECI)
REC = RECI[random.randint(0, len(RECI)-1)].rstrip()
print(REC)
#REC = "stagod"
def provera(pokusaj1):
    h = 0
    for a in pokusaj1:
        if a=='_':
            h+=1
    if h>0:
        return True

    return False


def kraj(k,pokusaj):
    if(BROJ_ZIVOTA-k > 0 and provera(pokusaj)):
        return True
    return False

def proverislovo(slovo):
    a = 0
    niz = []
    for i in REC:
        if i == slovo:
            niz.append(a)
        a+=1
    if niz:
        return niz
    return -1

pokusaj = []
for i in range(len(REC)):
    pokusaj.append('_')

k = 0
while(kraj(k,pokusaj)):
    slovo = input("Unesi neko slovo: ")
    if(proverislovo(slovo) != -1):
        for i in proverislovo(slovo):
            pokusaj[i] = slovo
        print(pokusaj)
    else:
        k+=1
        print(pokusaj)
        print("Preostali broj zivota: %d" % (BROJ_ZIVOTA-k))
    
print("Kraj!!!!")
print(REC)

