#Ardışık sayıların toplamı versiyon 2

# Kullanıcıdan limit al
limit = int(input("Sınır: "))

toplam = 0  # Ardışık sayıların toplamı
sayi = 1    # Başlangıç sayısı
terimler = []  # Hesaplamayı göstermek için liste

# Toplam limitten küçük olduğu sürece devam et
while toplam < limit:
    toplam += sayi
    terimler.append(str(sayi))  # Sayıyı listeye ekle
    sayi += 1

# Sonucu ve yapılan işlemi ekrana yazdır
print(f"Ardışık toplam: {' + '.join(terimler)} = {toplam}")