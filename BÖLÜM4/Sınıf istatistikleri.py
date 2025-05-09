# Dersin not istatistiklerini yazdıran program
def calculate_grade(exam_points, exercise_points):
    """
    Sınav puanları ve alıştırma puanlarına göre not seviyesini hesaplar.

    Parametreler:
        exam_points: 0-20 arası sınav puanı
        exercise_points: 0-10 arası alıştırma puanı

    Dönüş Değeri:
        0-5 arası not seviyesi
    """
    # Sınav kesme eşiği kontrolü
    if exam_points < 10:
        return 0

    total_points = exam_points + exercise_points

    if total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5

def convert_exercises_to_points(exercises):
    """
    Tamamlanan egzersiz sayısını puana dönüştürür.
    Her %10'luk tamamlama 1 puan verir (en fazla 10 puan).

    Parametreler:
        exercises: 0-100 arası tamamlanan egzersiz sayısı

    Dönüş Değeri:
        0-10 arası egzersiz puanı
    """
    return exercises // 10  # Aşağı yuvarlama yapılır

# Ana program
exam_points_list = []
exercise_points_list = []
grades = [0, 0, 0, 0, 0, 0]  # 0-5 arası notların sayısı

# Kullanıcıdan veri toplama
while True:
    user_input = input("Sınav puanları ve tamamlanan alıştırmalar: ")
    if user_input == "":
        break

    parts = user_input.split()

    # Giriş doğrulama
    if len(parts) != 2:
        print("Geçersiz giriş, lütfen iki sayı girin! 1. sayı 0-20 2. sayı 0-100 arası olsun")
        continue

    try:
        exam = int(parts[0])
        exercises = int(parts[1])
    except ValueError:
        print("Geçersiz giriş, lütfen geçerli sayılar girin!")
        continue

    # Eğer sınav veya alıştırma puanları belirtilen aralıkta değilse
    if not (0 <= exam <= 20) or not (0 <= exercises <= 100):
        print("Geçersiz sınav puanı veya alıştırma sayısı!")
        continue

    exam_points_list.append(exam)

    # Egzersizleri puana dönüştür
    exercise_points = convert_exercises_to_points(exercises)
    exercise_points_list.append(exercise_points)

    # Not hesapla ve ilgili not seviyesinin sayısını artır
    grade = calculate_grade(exam, exercise_points)
    grades[grade] += 1

# İstatistikleri yazdırma
print("İstatistikler:")

# Puan ortalaması
if exam_points_list:
    average = sum(exam_points_list) / len(exam_points_list)
    print(f"Puan ortalaması: {average:.1f}")
else:
    print("Puan ortalaması: 0.0")

# Başarı yüzdesi (sıfır olmayan not alanların yüzdesi)
total_students = sum(grades)
if total_students > 0:
    passed_students = total_students - grades[0]
    pass_percentage = (passed_students / total_students) * 100
    print(f"Başarı yüzdesi: {pass_percentage:.1f}")
else:
    print("Başarı yüzdesi: 0.0")

# Not dağılımı
print("Not dağılımı:")
for i in range(5, -1, -1):
    stars = "*" * grades[i]
    print(f"  {i}: {stars}")