word=input("Please type a sentence or word")
print("*"*30)
sayi=(28-len(word))//2  #+1 e gerek yok çünkü zaten boşluk kadar eklenip yazılacak
word="*"+" "*sayi+word+" "*(28 - len(word) - sayi)+"*"
print(word)
print("*"*30)