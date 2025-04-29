# yaş hesaplama

name=input("What is yoru name? ")
year=int(input("Which year were you born? "))
while year>2025:
    year=int(input("please enter less than 2025: "))
print(f"Hi {name}, you will be {2025-year} at the end of 2025 ")