#hava durumuna göre ne giyileceğine karar veren program gelişmiş hali.
def kiyafet_onerisi(sicaklik, yagmur):
    if sicaklik > 20:
        if yagmur:
            return "Şort ve tişört giyin, yanınıza şemsiye almayı unutmayın."
        else:
            return "Kot pantolon ve tişört giyin."
    elif sicaklik > 10:
        if yagmur:
            return "Kot pantolon ve hafif bir ceket giyin, şemsiyenizi alın."
        else:
            return "Kot pantolon ve hafif bir ceket giyin."
    elif sicaklik > 5:
        if yagmur:
            return "Kalın mont, kazak ve su geçirmez botlar giyin."
        else:
            return "Mont ve kazak giyin."
    else:
        return "Atkı, bere ve eldiven ile kalın bir mont giyin."

sicaklik = int(input("Yarın hava durumu tahmini nedir? Sıcaklık: "))
yagmur_girdi = input("Yağmur yağacak mı (evet/hayır): ").strip().lower()

yagmur = yagmur_girdi == "evet"
print(kiyafet_onerisi(sicaklik, yagmur))