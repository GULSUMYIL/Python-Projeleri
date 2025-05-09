n=int(input("How many rows you want "))
rows="*"
while n>0:
  print(" "*n + rows)
  rows+="**"
  n-=1