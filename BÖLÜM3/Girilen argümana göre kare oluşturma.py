#girilen argümana göre kare oluşturma

def hash_square(x):
  for _ in range(x):# zaten verilen ifade kadar döner yani 3 kez
      print(x*"#") #x ile carpılarak yazılır yani 3 kez

hash_square(3)
print()
hash_square(5)