#sayıları bir önden bir arkadan yazdır
number=int(input("sayı giriniz: "))
i=1
while i<number:
  print(i)
  print(number)
  i=i+1
  number=number-1
  if i== number:
    print(i)