#foydalanuvchidan malumotlarni qabul qilamiz
word = input("Text kiriting: ")
find = input("Qaysi so'zni qidirayapsiz:")

#Kerakli index aniqlaymiz:
index = word.find(find)

#Index -1 emas ekanligini tekshiramiz agarda index -1 bulsa suz topilmadi deyilsin:
if index != -1:
    print(f"Siz qidirayotgan so'z {index} chi indexdan boshlanadi!")
else:
    print("So'z topilmadi")