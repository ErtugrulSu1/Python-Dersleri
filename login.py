user = {
    "username" : "E10",
    "pass" : "12345",
    "name" :"Ertuğrul Su"
}

login_Un=input("Kullanıcı Adınızı Giriniz : ")
login_Pass=input("Şifrenizi Giriniz : ")

if(login_Un == user["username"] and  login_Pass == user["pass"]):
    print("Giriş Başarılı")

else:
    print("Giriş Başarısız ! ")
    