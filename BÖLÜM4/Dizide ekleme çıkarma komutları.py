# ekleme ve çıkarma
numbers=[]
while True:

  print(f"şu anda liste {numbers}")
  işlem=input("ad(d), (r)emove or e(x)it: ").strip().lower()

  if işlem=="d":
    next_number = numbers[-1] + 1 if numbers else 1
    numbers.append(next_number)

  elif işlem== "r":
    if numbers:
      numbers.pop()

  elif işlem=="x":
    print("Bye...")
    break

  else:
    print("geçersiz işlem girdiniz: A,R,X bir tanesini giriniz: ")



