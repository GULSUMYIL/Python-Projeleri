number = 1/3
print(f"The number is {number:.2f}") # noktadan sonra iki karakter yazılacağını belirtir


names =  [ "Steve", "Jean", "Katherine", "Paul" ]
for name in names:
  print(f"{name:15} centre {name:>15}")#büyüktür olunca sağa yaslı oluyor
        #küçüktür olsa veya ilk taraftaki gibi olsa sola yaslı olur

#f-string'lerin kullanımı printkomutlarla sınırlı değildir. Değişkenlere atanabilir ve diğer string'lerle birleştirilebilirler:
name = "Larry"
age = 48
city = "Palo Alto"
greeting = f"Hi {name}, you are {age} years of age"
print(greeting + f", and you live in {city}")