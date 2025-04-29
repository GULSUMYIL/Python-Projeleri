#artık yıl hesaplama
#artık yıl= 4 e tam bölünen ve 100e tam bölünmeyen aynı zamanda da 400 e rtam bölünebilen sayılara artık yıl denir.
yıl=int(input("Bir yıl giriniz: "))

if (yıl %400==0) or(yıl %4==0 and yıl %100!=0):
  print(f"{yıl} artık yıldır")
else:
  print(f"{yıl} artık yıl degıldır")