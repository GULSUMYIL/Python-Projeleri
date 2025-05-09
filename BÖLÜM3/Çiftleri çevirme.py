#çiftleri çevirin
number=int(input("Sayı giriniz: "))
i=1
while i <=number:
  if i==number and i%2==1:
    print(i)
  elif i%2==1:
    print(i+1)
    print(i)
  i=i+1