#girilen puana göre bonus puanı hesaplama
puan=int(input("Kartınızda kaç puan var: "))
bonus1=puan*0.1+puan
bonus2=puan*0.15+puan
if puan<100:
  print(f"Bonusunuz %10 Şu anda {float(bonus1)} puanınız var")
else:
  print(f"Bonusunuz %15 Şu anda {float(bonus2)} puanınız var")