#şifre doğrulama
password= input("Bir şifre giriniz: ")
repeat_password= input("Şifreyi tekrar giriniz: ")
while True:
  if password != repeat_password:
      print("They do not match!")
      repeat_password= input("Şifreyi tekrar giriniz: ")
  else:
    print("User account created!")
    break