#öğrencileri belirlenen sayılara göre gruplara ayırma gelişmiş hali.
def grup_hesapla():
    # Kullanıcıdan öğrenci sayısını al
    ogrenci_sayisi = int(input("Lütfen dersteki öğrenci sayısını girin: "))

    # Kullanıcıdan grup büyüklüğünü al
    grup_buyuklugu = int(input("Lütfen her grubun kaç kişi olacağını girin: "))

    # Grup sayısını hesapla
    grup_sayisi = ogrenci_sayisi // grup_buyuklugu
    kalan = ogrenci_sayisi % grup_buyuklugu

    print(f"Toplam {grup_sayisi} tam grup oluşturuldu.")

    # Eğer öğrenci sayısı tam bölünmüyorsa, bir ekstra küçük grup olacak
    if kalan > 0:
        print(f"Ek olarak {kalan} kişilik bir küçük grup oluşturuldu.")

grup_hesapla()