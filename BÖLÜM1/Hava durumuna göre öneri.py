#Hava durumuna göre giyilecek kıyafete karar veren program
sıcaklık=int(input("hava durumu Sıcaklık Nedir? "))
yagmur=input("Yağmur yağacak mı(evet/hayır)? ")

if (sıcaklık>=20 and yagmur=="hayır"):
  print( "kot pantolon ve tişört giyin")
if (sıcaklık>=20 and yagmur=="evet"):
  print( "kot pantolon ve tişört giyin")
  print("Şemsiyenizi almayı unutmayın")
if (sıcaklık>=10 and sıcaklık<20 and yagmur=="hayır"):
  print(" kot pantolon ve bluz giyin")
if (sıcaklık>=10 and sıcaklık<20 and yagmur=="evet"):
  print(" kot pantolon ve bluz giyin")
  print("Şemsiyenizi almayı unutmayın")
if(sıcaklık<10 and yagmur=="hayır"):
  print(" kazak giyin")
if(sıcaklık<10 and yagmur=="evet"):
  print(" kazak giyin")
  print("Şemsiyenizi almayı unutmayın")