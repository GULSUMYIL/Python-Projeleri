#sayı piramidi oluşturma
number=int(input("sayı giriniz: "))
while number>0:
  i=0
  while i<number:
    print(f"{i }", end=" ")
    i=i+1
  print()
  number=number-1