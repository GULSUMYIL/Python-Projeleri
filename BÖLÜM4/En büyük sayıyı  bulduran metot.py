def greatest_number(sayi1,sayi2,sayi3):
  if sayi1>sayi2 and sayi1>sayi3:
    return sayi1
  elif sayi2>sayi1 and sayi2>sayi3:
    return sayi2
  else:
    return sayi3

greatest_number(6,3,8)