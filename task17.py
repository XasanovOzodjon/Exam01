#foydalanuvchidan malumot qabul qilamiz
score = int(input("Bal kiriting: "))

# foydalanuvchini balini if yordamida teshirib natijasini elon qilamiz
if 90 <= score <= 100:
    print("A (A'lo)")
elif 80 <= score <= 89:
    print("B (Yaxshi)")
elif 70 <= score <= 79:
    print("C (Qoniqarli)")
elif 60 <= score <= 69:
    print("D (Qoniqarsiz)")
elif 0 <= score <= 59:
    print("F (Rad)")
else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")