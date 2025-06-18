#kerakli uzgaruvchilarni yaratib va foydalanuvchidan malumot qabul qilamiz
age = int(input("Yoshingizni kiriting: "))
ticket_price = 100


#foydalanuvchimizni yoshini if yordamida tekshirib chegirmani hisoblap kansolga chiqaramiz
if age <= 6:
    result = ticket_price - ticket_price * 0.50
    print(f"Yakuniy narx: {result} so'm (50% chegirma qo'llanildi)")
elif 7 <= age <= 17:
    result = ticket_price - ticket_price * 0.20
    print(f"Yakuniy narx: {result} so'm (20% chegirma qo'llanildi)")
elif age > 60:
    result = ticket_price - ticket_price * 0.30
    print(f"Yakuniy narx: {result} so'm (30% chegirma qo'llanildi)")
else:
    result = ticket_price
    print(f"Yakuniy narx: {result} so'm")