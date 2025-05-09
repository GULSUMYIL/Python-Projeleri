#bir listeye öğeler ekleyin
adet=int(input("Kaç adet ürün: "))
urunler=[] # dizi oluşturmadan atama yapamayız

for i in range(1,adet+1):
  deger=int(input(f"Ürün {i} : "))
  urunler.append(deger)
print(urunler)

#Belirli bir yere ekleme
#dizinin boyutu esnektir genişler
#insert metodu ile yapılır
numbers=[1,2,3,4,5,6]
numbers.insert(0,10)
print(numbers)
numbers.insert(2,20)
print(numbers)


#öğeleri kaldırma
# pop metodu ile yapılır
my_list=[1,2,3,4,5,6]
my_list.pop(2) #2. indesi yani 3 değerini siler
print(my_list)
my_list.pop(3)
print(my_list)