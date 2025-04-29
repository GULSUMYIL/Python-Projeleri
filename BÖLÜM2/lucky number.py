kosul=True;# koşul ilk whilenın çalışması için true olarak ayarlandı
while(kosul):#ilk sefer hariç int değer girilmezse çalışmaya deevam edecek
 try:
   number=int(input("Please type a number: "))#hata olursa excepte girecek koşul false olmayack
   if number>100:
    print("The number is greater than 100")
    number=number-100
    print("How its value decrased by one hundred")
    print("Value now: "+str(number))
   print(str(number)+"must be a lucky number")
   print("Have nice day!")
   kosul=False#koşul sayı girilirse döngüden çıkacak girilmezse devam edecek
 except:
  print("Error please give a number!")