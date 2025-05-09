# bir öğenin değerini değiştir
my_list=[1,2,3,4,5]
while True:
  index=int(input("index girin: "))
  if index==-1:
    break
  yenideger=int(input("Yeni değer girin: "))
  my_list[index]=yenideger
  print(my_list)