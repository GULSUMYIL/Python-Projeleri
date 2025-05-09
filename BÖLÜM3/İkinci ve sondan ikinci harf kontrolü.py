#İkinci ve sondan ikinci karakerin aynı olup olmadığını kontrol eden program
# Kullanıcıdan bir metin girmesini isteyen program
metin = input("Lütfen bir metin girin: ")

# İkinci ve sondan ikinci karakterin aynı olup olmadığını kontrol et
if metin[1] == metin[len(metin) - 2]:
    print(f"İkinci ve sondan ikinci karakterler aynı: {metin[1]}")
else:
    print("İkinci ve sondan ikinci karakterler farklı.")


#ikinci ve sondan ikinci karakter
word=input("Kelime giriniz: ")
if len(word)<2:
  print("Uzunluğu en az 2 olan bi kelime giriniz")
else:
  if word[1]== word[-2]:
    print("kelimelerin 2. ve sondan 2. harfleri aynıdır")
  else:
    print("kelimelrin 2. ve sondan 2. harfleri aynı değildir")