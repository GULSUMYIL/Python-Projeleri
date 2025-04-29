#döngü içerisinde karekök hesaplama
from math import sqrt


while True:
  sayı=int(input("Tam sayı giriniz(0 döngüden çık): "))
  if sayı<0:
    print("Geçersiz sayı")
  elif sayı>0:
    print(f"girlen sayının karekökü {sqrt(sayı)}")
  else :
    print("döngüden çıklıyor")
    break
print("döngüden çıkıldı")