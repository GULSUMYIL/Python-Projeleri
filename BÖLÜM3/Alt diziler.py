#Alt diziler bölüm 1
girdi = input("Lütfen bir dize yazın: ")
sonuc = ""

for i in range(1, len(girdi) + 1):
    sonuc += girdi[:i] + " " # her seferinde sonucu 0 dan i degerine kadar döndürür

print(sonuc.rstrip()) #bir string'in sağ tarafındaki (sonundaki) boşlukları siler.


#Alt diziler bölüm 2
girdi = input("Lütfen bir dize yazın: ")
sonuc = ""

for i in range(1, len(girdi) + 1):
    sonuc += girdi[-i:] + " " # tersten sıralama yapması için -i kullandık

print(sonuc.rstrip())


#Alt dizilerde arama
#in ifadesi bir dizenin belirli bir alt parçacığı içerip içermediğini belirler
#bool ifadedir true ve false döndürür
input_str="test"
print("t" in input_str)
print("x" in input_str)
print("es" in input_str)
print("ets" in input_str)