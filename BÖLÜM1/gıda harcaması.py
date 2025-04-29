# gıda harcaması
gün_sayisi=int(input("Haftada kaç kez öğrenci kafetaryasında yemek yiyorsunuz? "))
fiyat_yemek=float(input("Günlük yemeğin fiyatı nedir? "))
fiyat_market=float(input("Günlük markete ne kadar harcama yapıyorsunuz? "))
aylık_yemek=gün_sayisi*fiyat_yemek*4
aylık_market=gün_sayisi*fiyat_market*4
print(f"Aylık yemeğe harcanan fiyat:{ aylık_yemek} TL")
print(f"Aylık markete harcanan fiyat:{ aylık_market} TL")