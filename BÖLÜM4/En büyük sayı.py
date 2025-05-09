# en büyük sayı

def greatest_number(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  else:
    return c

print(greatest_number(3, 4, 1))
print(greatest_number(99, -4, 7))
print(greatest_number(0, 0, 5))