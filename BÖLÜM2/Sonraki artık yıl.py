#bir sonraki artık yıl hesaplama
# Kullanıcıdan yılı al
year = int(input("Yıl: "))

# Artık yıl kontrolü fonksiyonu
def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

# Sonraki artık yılı bul
next_leap_year = year + 1
while not is_leap_year(next_leap_year):
    next_leap_year += 1

# Sonucu ekrana yazdır
print(f"{year}'ten sonraki artık yıl {next_leap_year}'tir.")