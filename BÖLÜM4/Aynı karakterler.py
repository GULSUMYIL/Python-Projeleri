#Aynı karakterler
def same_chars(kelime,a,b):
  i=0
  if a<0 or b<0 or a>=len(kelime) or b>=len(kelime):
    return False # sınır dışı index varsa 0 döndürür
  return kelime[a]==kelime[b]
print(same_chars("programmer", 6, 7))
print(same_chars("programmer", 0, 4))  # False
print(same_chars("hello", 1, 10))      # False (İndeks sınır dışında)
print(same_chars("test", 2, 2))