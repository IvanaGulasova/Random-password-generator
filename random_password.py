import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

num_letters = int(input("How many letters do you want in your password: \n"))
num_num = int(input("How many numbers do you want in your password: \n"))
num_characters = int(input("How many special characters do you want in your password: \n"))

rand_lett = random.choices(letters, k=(num_letters))
rand_num = random.choices(numbers, k=(num_num))
rand_char = random.choices(special_char, k=(num_characters))

all_random = rand_lett + rand_num + rand_char
random.shuffle(all_random)


print(f"Generated password: " , *all_random, sep= '')