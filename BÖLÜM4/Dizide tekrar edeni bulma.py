#liste ve dizilerde tekrar edeni bulmak için .count metodunu kullanırız.
my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
print(my_string.count("ch"))

my_list = [1,2,3,1,4,5,1,6]
print(my_list.count(1))

my_string = "Hi there"
new_string = my_string.replace("Hi", "Hey")#hi ifadesini hey ile değiştirir
print(new_string)

sentence = "sheila sells seashells on the seashore"
print(sentence.replace("she", "SHE"))

my_string = "Python is fun"
#bu durumda python yazar. cünkü atama yapmadğımız kısmı aktarıyor
my_string.replace("Python", "Java")
print(my_string)
#java yazsın istiyorsak atama yapabiliriz
my_string = my_string.replace("Python", "Java")
print(my_string)