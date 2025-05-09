#çarpım tablosu oluşturma
number1=int(input("sayı1 giriniz: "))

for i in range(1,number1+1):
  for j in range(1,number1+1):
    print(f"{i}x{j}={i*j}")