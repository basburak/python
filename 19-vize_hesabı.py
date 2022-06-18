vize1= int(input("İlk sınavı giriniz :"))
vize2= int(input("ikinci sınavı giriniz :"))
final = int(input("final sınavını giriniz :"))

notunuz = vize1*0.3 + vize2*0.3 + final*0.4

if notunuz >= 90 :
    print("AA")
elif notunuz >=85 :
    print("BA")
elif notunuz >=80 :
    print("BB")
elif notunuz >=75 :
    print("CB")
elif notunuz >=70 :
    print("CC")
elif notunuz >=65 :
    print("DC")
elif notunuz >=60 :
    print("DD")
else: 
    print("FF")
