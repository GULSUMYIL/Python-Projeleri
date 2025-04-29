#ikinci dereceden denklemin köklerini hesaplama.
#from math import sqrt# matematik sınıfından karekök almayı import ettik
#print(sqrt(9)) 3.0 olarak çıktısını verir
#print(pow(2,3)) 8 oalrak çıktısını verir

from math import sqrt  # sqrt fonksiyonunu içe aktarıyoruz.

# Kullanıcıdan a, b ve c değerlerini al
a = float(input("a'nın değeri: "))
b = float(input("b'nin değeri: "))
c = float(input("c'nin değeri: "))

# Diskriminantı hesapla: b² - 4ac
discriminant = b**2 - 4*a*c

# İkinci dereceden denklemin köklerini hesapla
x1 = (-b + sqrt(discriminant)) / (2 * a)
x2 = (-b - sqrt(discriminant)) / (2 * a)
4
# Sonucu ekrana yazdır
print(f"Kökler {x1} ve {x2}'dır.")