 lines (67 sloc) 1.67 KB
def arithmetic(a: float,b:float,c:str):
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param float c: Aritmeetilene tehing
    :rtype float:
    """
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b 
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            print("Div0")
            r=0.0
    else:
        print("Viga")
        r=0.0
    return r

def is_year_leap(aasta: int):
    """Liigaasta
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsiooni vastus logilises formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

def square(a):
    """Ruudu külg
    Annab vastust ruudu pindala,diogonaal,ümbermõõt
    :param int külg: Kui pikk külg
    :rtype bool:Funktsiooni vastus valemi järgi
    """
    p = 4*a
    s = a*a
    d = (a**2) / 2
    k = (p, s, d)
    return k

def season(number):
    """Aastaajad
    Saab vastust kuu aastaaja järgi
    :param int number:Kuu
    :rtype bool:Funktisooni järgi saame vastust milline aastaaja on
    """
    if number == 12 or 1 <= number <= 2:
        print("Talv")
    elif  3 <= number <= 5:
        print("Kevad")
    elif 6 <= number <= 8:
        print("Suvi")
    elif 9 <= number <= 11:
        print("Sügis")
    else:
        print("Kirjuta ainult aastaajad")
    n = int(input("Kirjuta kuu numbritega : "))
    return n

def xor_cipher(string: str, key:str)->str:
    """Tavaline sõna kodeeritakse
    """
    result = ''
    temp = int()
    for i in range(len(key)):
        temp = ord(string[i]) #näitab sümboli
          kood
        for j in range(len(key)):
            temp ^= ord(key[j])
        result += chr(temp)
    return result
