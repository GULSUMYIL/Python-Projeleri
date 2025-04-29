#Öğrencileri belirlenen sayılarda gruplara ayırma
ogr_sayisi=int(input("Öğrenci sayısını giriniz: "))
grup_byk=int(input("İstenilen grup büyüklüğünü giriniz: "))
if ogr_sayisi % grup_byk == 0:
  print(f"Oluşturulan grup sayısı: {ogr_sayisi/grup_byk}")
else:
  print(f"Oluşturulan grup sayısı: {ogr_sayisi//grup_byk+1}")