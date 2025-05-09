#bir dizideki tüm karakterleri baştan sona sıralar
kelime=input("Bir kelime giriniz: ")
harf=0
while harf<len(kelime):
  print(kelime[harf])
  harf +=1
print("Last character: " + kelime[-1])#en sondaki kelimeyi ifade eder

#sondan başa yazdırma
word=input("Kelime giriniz: ")
for char in reversed(word): # kelimelerin harflerini sondan başa yazdırır
    print(char)