# Pazar günü çalışmaları için 2 kat ücret hesaplayan ve maaşı yazdıran program

saatbasi = int(input("Saat başı ücret ne kadar? "))
saat = int(input("Kaç saat çalıştınız? "))
gun = input("Çalıştığınız gün nedir? ")

# Gün ismini büyük harfe çevirerek kontrol ediyoruz
if gun.upper() == "PAZAR":
    kazanc = saat * saatbasi * 2
else:
    kazanc = saat * saatbasi

print(f"Kazancınız: {kazanc} TL")

