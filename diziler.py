#List Örneği
isimler=["Ertuğrul", "Emir", "Elanur"]

print(isimler)

isimler[2]="Ahmet"

print(isimler)
 
######################
#Tuple Kullanımı
yaslar=(10,11,15)

print(yaslar)

#yaslar[2]=13

#print(yaslar) Tuple Değiştirilemez

##################
#Dictionary
"""
arac={
    "plaka" : "10 ERT 10",
    "Renk" : "Kırmızı",
    "Marka" : "BMW",
    "Model" : "520d"
}
print(arac)
"""

user={
    "username" : "Ert10",
    "password" : "12345",
    "mail" : "ert10@gmail.com"
}

print(user["username"])