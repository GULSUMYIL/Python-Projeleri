#sayılarla çalışmak: ortalamaları ve pozitif sayıları negatif sayıalrı ayırarak yazmak.
# Sayıları takip etmek için değişkenler
count = 0          # Girilen sayı adedi
total = 0          # Sayıların toplamı
positive_count = 0 # Pozitif sayı adedi
negative_count = 0 # Negatif sayı adedi

print("Lütfen tam sayı girin. Bitirmek için 0 girin.")

while True:
    number = int(input("Sayı: "))

    if number == 0:  # Kullanıcı 0 girerse döngü sonlanır
        break

    count += 1       # Sayı adedini artır
    total += number  # Sayıyı toplama ekle

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

# Sonuçları ekrana yazdır
print(f"Girilen sayı adedi: {count}")
print(f"Sayıların toplamı: {total}")

# En az bir sayı girildiği varsayılıyor, dolayısıyla bölme hatası olmaz.
average = total / count
print(f"Sayıların ortalaması: {average:.1f}")

print(f"Pozitif sayılar: {positive_count}")
print(f"Negatif sayılar: {negative_count}")