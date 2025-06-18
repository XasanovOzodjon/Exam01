
#kerakli uzgaruvchilarni yaratib va foydalanuvchidan malumot qabul qilamiz
weight = float(input("Vazn: "))
height = float(input("Bo'y: "))
check = True

#Foydalanuvchi vazn va bo'yni to'g'ri kiritimi shuni tekshiriamiz
if weight <= 0 and height <= 0:
    check = False
if height < 0.5 or 3.0 < height:
    check = False
if weight < 1 or 500 < weight:
    check = False
    
#Agar foydalanuvchi to'g'ri kiritgan bulsa BMI hisoblaymiz aks xolda Xato kiritingiz degan yozuvni chiqaramiz
if check:
    BMI = round(weight / (height ** 2), 2)
    if BMI < 18.5:
        result = "Kam vazn"
    elif 18.5 <= BMI < 25:
        result = "Normal vazn"
    elif 25 <= BMI < 30:
        result = "Ortiqcha vazn"
    elif BMI >= 30: 
        result = "Semizlik"
        
    print(f"BMI: {BMI}\nTasnif: {result}")
else:
    print("Siz bo'y yoki vaznni xato kiritingiz")