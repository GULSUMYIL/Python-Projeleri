#ilk ikinci ve son kelimeler
#split() metodu, cümleyi boşluklardan ayırarak bir kelime listesi oluşturur.
def first_word(cümle):
  return cümle.split()[0] #hazır metot kullanarak sıraladık
def second_word(cümle):
  return cümle.split()[1]
def last_word(cümle):
  return cümle.split()[-1] # son elemanı döndürüyor
cumle="it was a dark and stormy python"
print(first_word(cumle))
print(second_word(cumle))
print(last_word(cumle))