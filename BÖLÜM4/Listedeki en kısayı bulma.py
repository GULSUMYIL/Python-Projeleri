# listedeki en kısayı bulma

def shortest(list):
  if not list:
    return 0
  short = list[0]

  for kısa in list:
    if len(kısa)<len(short):
      short=kısa

  return short # eğer ki len içerisinde yazarsam kelimenin uzunluğunu döndürür

my_list = ["first", "second", "fourth", "eleventh"]

result = shortest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = shortest(my_list)
print(result)