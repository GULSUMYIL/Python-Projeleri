word_list=[]
while True:
 word=input("please type a word ")
 if word in word_list:
  break
 word_list.append(word)

print(word_list)