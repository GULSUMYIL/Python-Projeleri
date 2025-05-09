#bir argüman veya dönüş değeri olarak bir liste
def median(my_list: list):
    ordered = sorted(my_list)
    list_centre = len(ordered) // 2 # tam sayı olmalıdır
    return ordered[list_centre]
shoe_sizes = [45, 44, 36, 39, 40]
print("The median of the shoe sizes is", median(shoe_sizes))

ages = [1, 56, 34, 22, 5, 77, 5]
print("The median of the ages is", median(ages))

# büyük sayı ve medyanı bulma
def input_numbers():
    numbers = []
    while True:
        user_input = input("Please type in an integer, leave empty to exit: ")
        if len(user_input) == 0:
            break
        numbers.append(int(user_input))
    return numbers
numbers = input_numbers()

print("The greatest number is", max(numbers))
print("The median of the numbers is", median(numbers))