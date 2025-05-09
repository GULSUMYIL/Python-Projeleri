#Ardışık sayıların toplamı versiyon 1
limit = int(input("Sınır: "))

toplam = 0  # Ardışık sayıların toplamı
sayi = 1    # Başlangıç sayısı

# Toplam limitten küçük olduğu sürece devam et
while toplam < limit:
    toplam += sayi
    sayi += 1

# Sonucu ekrana yazdır
print(toplam)