#Mantıksal operatörler
note=int(input("What is student exam note: "))
if note>=0 and note<=49:
  print("Student fail on the exam")
elif note>=50 and note<=59:
  print("1")
elif note>=60 and note<=69:
 print("2")
elif note>=70 and note<=79:
  print("3")
elif note>=80 and note<=89:
  print("4")
elif note>=90 and note<=100:
  print("5")
else:
  print("Exam not must be between 0 and 100")