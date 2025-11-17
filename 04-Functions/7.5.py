def funkcja(x,y,z):
    if z <= y and z >= x:
        return True
    else:
        return False
l1 = input("podaj 1 wartosc zakresu: ")
l2 = input("podaj 2 wartosc zakresu: ")
l3 = input("podaj sprwdzana lioczbe: ")

if funkcja(l1,l2,l3):

    print("jest w zakresie")

else:
    print("nie jets w zakresie")