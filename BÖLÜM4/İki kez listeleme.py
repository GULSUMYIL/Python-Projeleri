#iki kez listeleme
liste=[]
while True:
  deger=int(input("Bir değer giriniz: "))
  if deger==0:
    print("Bye!")
    break

  liste.append(deger) # listeye yeni değer ekledik
  print(f"Şimdiki liste: {liste}")  # orjinal listeyi yazdırır
  print(f"Sıralı liste: {sorted(liste)}")  # sıralı listeyi yazdırdık