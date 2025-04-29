#kelimeleri alfabetik sıraya göre sıralama
word1=input("Please enter first word: ")
word2=input("Please enter second word: ")
if word1.upper()<word2.upper():
  print("First word comes first in alpahabet")
elif word1.upper()>word2.upper():
  print("Second word comes first in alpahabet")
else:
  print("words are same")