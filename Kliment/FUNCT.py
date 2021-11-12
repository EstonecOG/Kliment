from module1 import *
while True:
    print("Funktsioonid" .center(50,"+"))
    print("arithmetic- A,is_year_leap-Y,square-N,O-season")
    v=input()
    if v.upper()=="A":
        arv1=float(input("Arv 1:"))
        arv2=float(input("Arv 2:"))
        sym=input("Tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=="Y":
        rezult=is_year_leap(int(input("Sissesta aasta")))
        print(rezult)
    elif v.upper()=="N":
        rezult=square(int(input("Sissesta külje pikkus")))
        print(rezult)
    elif v.upper()=="O":
        rezult=season(int(input("Sissesta kuu numbritega")))
        print(rezult)
        w