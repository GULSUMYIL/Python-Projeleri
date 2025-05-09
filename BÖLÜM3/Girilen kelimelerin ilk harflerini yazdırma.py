sentence = input("Please type a sentence")  # Kullanıcıdan cümle al
sentence = " " + sentence  # Başına boşluk ekleyerek ilk harfin algılanmasını sağla
i = 0

while i < len(sentence) - 1:
    if sentence[i] == " ":
        print(sentence[i + 1])  # Boşluktan sonraki harfi yazdır
    i += 1  # İndeksi artır