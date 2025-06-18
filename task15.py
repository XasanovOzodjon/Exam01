#foydalanuvchidan malumot qabul qilamiz
number = int(input("Son kiritng: "))

#foydalanuvchidan olgan sonimiz 2 ga yoki 3 ga yoki 5 ga bo'linadimi yoki yuq shuni tekshiramiz 
if number % 2 == 0:
    print(f"{number} soni 2 ga bo'linadi")
elif number % 3 == 0:
    print(f"{number} soni 3 ga bo'linadi")
elif number % 5 == 0:
    print(f"{number} soni 5 ga bo'linadi")
else:
    print(f"{number} soni 2,3,5 ning hech qaysiga bo'linmaydi.")