#çift sayılar

def even_numbers(dizi):
  yenidizi=[] #iki dizi olusturmak icin bos bir tane tanımladık
  for cift in dizi:
    if cift %2==0:
      yenidizi.append(cift) # append ile eklemeyı yapmak daha kolay unutma
  return yenidizi #return ifadesi ile metot döndürülmeli yoksa none gönderir

my_list = [1, 2, 3, 4, 5,9,15,48]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)