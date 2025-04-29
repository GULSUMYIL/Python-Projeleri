#sonucu boolean cinsinden gösteren hesaplama
sayi1=int (input("Bir sayı giriniz "))
sayi2=int (input("İkinci sayıyı giriniz "))
operation=input("Lütfen +,-,* veya / birinizi giriniz")
if (operation=='+'):
  print(sayi1+sayi2)
if(operation=='-'):
  print(sayi1-sayi2)
if(operation=='*'):
  print(sayi1*sayi2)
if(operation=='/'):
  print(sayi1/sayi2)