#faktöriyel hesaplama hazır metot
import math

while True:
    number = int(input("Lütfen bir tam sayı girin: "))
    if number <= 0:
        break

    # Faktöriyel hesaplanır ve yazdırılır
    print(f"{number}! = {math.factorial(number)}")#hazır metot


#faktöriyel hesaplama hazır metot kullanmadan
while True:
    number = int(input("Lütfen bir tam sayı girin: "))

    # 0 veya negatif girilirse döngü sonlanır
    if number <= 0:
        break

    # Faktöriyel hesaplama
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    # Sonucu ekrana yazdır
    print(f"{number}! = {factorial}")  