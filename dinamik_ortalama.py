toplam=0
sayac=0
while True:
    sayi=input("Sayi => ")
    if sayi=='q':
        break
    else:
        toplam+=int(sayi)
        sayac+=1


print(toplam)
print(toplam/sayac)

