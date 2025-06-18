#foydalanuvchidan malumot qabul qilamiz
doc = input("Document nomini kiriting: ")

# documentimiz formati .pdf , .docx yoki .txt format bilan tugayaptimi yoki yuqligini tekshiramiz
if doc.endswith(".pdf") or doc.endswith(".docx") or doc.endswith(".txt"):
    result = True
else:
    result = False
    
# Natijani konsolga chiqarish
print(result)