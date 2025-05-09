# kelimelerden hangisi daha uzun ise onu yazdıran program
kelime1=input("1. kelimeyi giriniz: ")
kelime2=input("2. kelimeyi giriniz: ")
if len(kelime1)>len(kelime2):
  print(f"{kelime1} daha uzundur {kelime2} den")
else:
  print(f"{kelime2} daha uzundur {kelime1} den")