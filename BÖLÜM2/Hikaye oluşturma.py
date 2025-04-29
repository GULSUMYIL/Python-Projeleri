# kelimeleri girerek hikaye oluştur 
# Kelimeleri saklamak için liste
story = []

# Önceki kelimeyi takip etmek için değişken
previous_word = ""

while True:
    word = input("Lütfen bir kelime yazın: ")

    # Kullanıcı "end" yazarsa döngüden çık
    if word.lower() == "end":
        break

    # Kullanıcı aynı kelimeyi arka arkaya yazarsa döngüden çık
    if word == previous_word:
        break

    # Hikayeye kelimeyi ekle
    story.append(word)

    # Önceki kelimeyi güncelle
    previous_word = word

# Hikayeyi birleştirerek yazdır
print("\nHikaye:", " ".join(story))