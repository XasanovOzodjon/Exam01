#kerakli uzgaruvchilarni yaratib va foydalanuvchidan malumot qabul qilamiz
text = input("Text kiriting:")
vowels = "aeiou"
vowels_cound = 0

#for yordamida unlilarni tekshirish jarayoni, sikl tugagandan keyn unlilar soni 0 ta emasligini tekshiramiz
for char in text:
    if char in vowels:
        vowels_cound += 1
else:
    if vowels_cound == 0:
        vowels_cound = "Unli harflar topilmadi"

# Natijani konsolga chiqarish
print(f"'{text}' -> {vowels_cound}")