#kelimelerin ilk harflerini ekrana yazdırma
cumle=input("Bir cümle giriniz: ")
cumle=" "+ cumle # başına boşluk ekledim cünkü ilk harfide algılamalı
i=0
while i<len(cumle)-1:
  if cumle[i]==" ":
    print(cumle[i+1]) # boşluktan bir sonraki harfi yazdırır
  i+=1