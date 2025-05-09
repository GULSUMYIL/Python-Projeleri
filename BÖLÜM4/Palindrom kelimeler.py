#palindromlar(düz ve ters yazımı aynı olan kelimelerdir: küçük, radar vb.)
def palindromes(dizi):
  dizi=dizi.lower()
  return dizi==dizi[::-1] #diziyi tersten yazdırma

while True:
    word = input("Lütfen bir kelime girin: ")
    if palindromes(word):
        print(f"{word} bir palindromdur!")
        break
    else:
        print(f"{word} bir palindrom değildir. Tekrar deneyin.")