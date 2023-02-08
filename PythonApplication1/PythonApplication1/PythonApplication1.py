from module1 import * 
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
while True:
    print(palgad)
    print(inimesed)
    menu=int(input("Valik:\n 1-Lisa andmed\n 2-Remove andmed\n 3-Max andmed\n 4-min andmed\n 5-sort andmed\n"))
    if menu==0:
        break
    elif menu==1:
        inimesed,palgad=Lisa_andmed(inimesed,palgad)
    elif menu==2:
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif menu==3:
        palk,nimi=suur(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}´l")
    elif menu==4:
        palk,nimi=väike(inimesed,palgad)
        print(f"Väike palk on {palk} {nimi}´l")
    elif menu==5:
        inimesed,palgad=sortirovka(inimesed,palgad)
    elif menu==6:
        palk,nimi=dublikate(inimesed,palgad)