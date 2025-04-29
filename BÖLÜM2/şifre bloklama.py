#3 girişten sonra girlen şifre yanlışsa şifreyi bloklayan program.
sayac=3
attempt=0 #giriş
while sayac>0:#3 hakktan sonra kart bloke edilemeli
  code=input("Please type your pin: ")
  attempt=attempt+1
  if code=="1234":
    print(f"Pin is correct it took {attempt} attempts")
    break
  else:
    sayac=sayac-1
    if sayac>0:
      print("Pin is false please try again")
    else:
      print("Your card is blocked now")