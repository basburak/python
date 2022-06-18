print("""*********************
Kullanıcı Girişi
************************""")
sys_kullanıcı_adı =("burak")
sys_parola = ("12345")

kullanıcı_adı = (input("Kullanıcı adı giriniz : "))
parola = (input("parolanızı giriniz : "))

if(kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("parolanız hatalı")
elif(kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print("kullanıcı adınız hatalı")
elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("kullanıcı adı ve parola hatalı")
else:
    print("kullaıcı adı ve parola doğru")
    print("Başarıyla giriş sağlanıyor...")
