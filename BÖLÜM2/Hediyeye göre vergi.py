#hediye fiayatına göre vergi alımı
gift_value = int(input("Gift price: "))  # Hediye fiyatı alınıyor

# Vergi hesaplama
if gift_value >= 5000 and gift_value < 25000:
    tax_value = 100 + (gift_value - 5000) * 8 / 100
elif gift_value >= 25000 and gift_value < 55000:
    tax_value = 1700 + (gift_value - 25000) * 10 / 100
elif gift_value >= 55000 and gift_value < 200000:
    tax_value = 4700 + (gift_value - 55000) * 12 / 100
elif gift_value >= 200000:
    tax_value = 22000 + (gift_value - 200000) * 14 / 100
else:
    print("No tax!")
    tax_value = 0  # Vergi yoksa tax_value sıfır olarak ayarlanmalı

# Vergi çıktısı
print(f"The tax of gift: {tax_value}")  # f-string kullanımı ile hatasız çıktı