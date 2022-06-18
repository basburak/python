print("""********************
Hesap Makinesi
İşlemler ;

1. Toplama İşlemi
2. Çarpma İşlemi
3. Çıkarma İşlemi 
4. Bölme İşlemi

**************************""")

a= int(input("Sayı Giriniz : "))
b= int(input("Sayı Giriniz : "))

işlem = input("İşlemi Giriniz : ")
if işlem =="1":
    print(f"{a} ile {b} in Toplamı {a+b} dır.")
elif işlem == "2":
    print(f"{a} ile {b} in Çarpımı {a*b} dır.")
elif işlem == "3":
    print(f"{a} ile {b} in Farkı {a-b} dır.")
elif işlem == "4":
    print(f"{a} ile {b} in Bölme {a/b} dır.")
else: 
    print("Geçersiz İşlem")
