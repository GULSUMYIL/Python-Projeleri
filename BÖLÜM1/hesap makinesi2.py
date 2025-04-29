#hesap makinesi 2
sayi1 = int(input("sayı giriniz 1 :"))
sayi2 = int(input("sayı giriniz 2 :"))
işlem = input("işlem: ")

if(işlem == "toplama"):
  print(f"{sayi1}+{sayi2}={sayi1+sayi2}")
if(işlem == "çıkarma"):
  print(f"{sayi1}-{sayi2}={sayi1-sayi2}")
if(işlem == "çarpma"):
  print(f"{sayi1}*{sayi2}={sayi1*sayi2}")
if(işlem == "bölme"):
  print(f"{sayi1}/{sayi2}={sayi1/sayi2}")