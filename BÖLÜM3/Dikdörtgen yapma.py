#dikdörtgen yapma
height=int(input("please type height information"))
weight=int(input("please type weight information"))
control1=1
control2=1
while control1<weight:
  while control2<=height:
    print("#"*weight)
    control2 +=1
  control1 +=1