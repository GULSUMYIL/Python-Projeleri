#girilen 2 yaşın kıyaslaması
person1_name=input("What is person 1 name: ")
person1_age=int(input("What is person 1 age: "))
person2_name=input("What is person 2 name: ")
person2_age=int(input("What is person 2 age: "))
if person1_age<person2_age:
  print(person2_name+" is bigger than "+person1_name)
elif person1_age>person2_age:
  print(person1_name+" is bigger than "+person2_name)
else:
  print("Both are at sama age")