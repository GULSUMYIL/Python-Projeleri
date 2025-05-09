# ladin ağacı çizimi
def spruce(x):
  sekil="*"
  bosluk=x
  while x>0:
    print(" "*x+sekil)
    x=x-1
    sekil+="**"
  print(" "*bosluk+"*")# x i bosluka atadık çünkü diğer türlü x döngüden sonra durucak

spruce(3)
print()
spruce(5)