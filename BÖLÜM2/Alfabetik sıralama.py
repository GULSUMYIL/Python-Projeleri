#alfebetik olarak ortada olan keimeyi bulma
a=input("bir kelime giriniz: ")
b=input("2. kelime giriniz: ")
c=input("3. kelime giriniz: ")

harfler=[a,b,c]
harfler.sort() # dizideki indisleri alfebetik olarak sıralar

print(f"ortadaki kelime  {harfler[1]}")