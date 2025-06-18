#foydalanuvchidan malumot qabul qilamiz
char = input("Iltimos Harf kiriting: ")

#Natijani Xisoblash jarayoni:
if char.isalpha() and ord(char) < 91:
    result = True
else:
    result = False
    
# Natijani konsolga chiqarish
print(result)