def Lisa_andmed(i:list,p:list):
    """Kirjeldus
    Lisa element list
    :param list i: Inimeste järjend
    :param list p: Palgad järjend
    :rtype: list, list 
    """
    n=int(input("Mitu inimesed: "))
    for j in range(n):
        x=input("Lisa inimesi: ")
        y=int(input("Lisa palk: "))
        p.append(y)
        i.append(x)
    return(i,p)
def kustutamine(i:list,p:list):
    """Kirjeldus
    Delete element list
    :param list i: Inimeste järjend
    :param list p: Palgad järjend
    :rtype: list, list 
    """
    name=input("Sisesta nimi: ")
    if name in i:
        arv=i.count(name)
        for a in range(arv):
            ind=i.index(name)
            i.pop(ind)
            p.pop(ind)
    return (i,p)
def suur(i:list,p:list):
    """Kirjeldus
    max element list
    :param list i: Inimeste järjend
    :param list p: Palgad järjend
    :rtype: list, list 
    """
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi
def väike(i:list,p:list):
    """Kirjeldus
    max element list
    :param list i: Inimeste järjend
    :param list p: Palgad järjend
    :rtype: list, list 
    """
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi
def sortirovka(i:list,p:list):
    """Kirjeldus
    max element list
    :param list i: Inimeste järjend
    :param list p: Palgad järjend
    :rtype: list, list 
    """
    v=int(input("palk 1-kahaneb,2-kasvab?: "))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                   abi=p[j]
                   p[j]=p[k]
                   p[k]=abi
                   abi=i[j]
                   i[j]=i[k]
                   i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                   abi=p[j]
                   p[j]=p[k]
                   p[k]=abi
                   abi=i[j]
                   i[j]=i[k]
                   i[k]=abi
    return i,p
def dublikate(i:list,p:list):
    """Kirjeldus
    max element list
    :param list i: Inimeste järjend
    :param list p: Palgad järjend
    :rtype: list, list 
    """
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid))
    for palk in dublikatid:
        n=p.count(palk)
        k=-1
        print(palk)
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi)