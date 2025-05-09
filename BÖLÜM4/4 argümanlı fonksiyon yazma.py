# 4 argüman alan fonksiyon yazma

def shape(a,b,c,d):
  i=1
  while i<=a:
    print(i*b)
    i+=1
  for _ in range(c):
    print(c*d)

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")