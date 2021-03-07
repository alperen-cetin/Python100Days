# #Challenge1: Area Calculator
# import math
# def paint_calculation(height,width,cover):
#     res = math.ceil((height * width) / cover)
#     print(f"You'll need {res} cans of paint.")


# test_height = int(input("Height Of Wall: "))
# test_width = int(input("Width Of Wall: "))
# coverage = 5
# paint_calculation(height =test_height,width = test_width,cover = coverage)

# #Challenge2: Prime Number Checker
# def prime_checker(number):
#     for i in range(2,number):
#         if i % 2 == 0:
#             is_prime = False
#     if is_prime:
#         print("prime number")
#     else:
#         print("not")


# num = int(input("Number: "))
# prime_checker(number = num)

# #Challenge3: Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 
    'f', 'g', 'h', 'i', 'k', 'l', 'm', 
    'n', 'o', 'u', 'p', 'q', 'r', 's', 
    't', 'v', 'x', 'y', 'z','a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'k', 'l', 'm', 'n', 'o', 'u', 'p', 
    'q', 'r', 's', 't', 'v', 'x', 'y', 'z']

def cipher(t,s,d):
    res = ""
    if s > 24:                  # shift = shift % 26 would give the same result
        x = s % len(alphabet)
        s = x
    if d == "decode":
        s *= -1
    for i in t:
        if i in alphabet:
            pos = alphabet.index(i)
            new_pos = pos + s
            res += alphabet[new_pos]
        elif i not in alphabet:
            res += i
    print(f"{d}d result is: {res}")


again = True
while again:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt.")
    text = input("Your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(t = text,s=shift,d=direction)
    answer = input("Would you like to run the program again? 'yes' or 'no'\n")
    if answer == "no":
        again = False

###### My Try. ### not working in long encryptions due to for loops
# def encrypt(t,s):
#     x = ""
#     for y in range(0,len(t)):
#         for i in range(0,len(alphabet)):
#             if alphabet[i] == t[y]:
#                     x += alphabet[i + s]
#     print(x)
# if direction == "encrypt":
#     encrypt(t = text, s = shift)
# elif direction == "decrypt":
#     encrypt(t = text,s = -shift)               
#### Tutor's Solution ### always working thx to .index() method
# def encrypt(t,s):
#     new_text = ""
#     for y in t:
#         pos = alphabet.index(y)
#         new_pos = pos + s
#         new_text += alphabet[new_pos]
#     print(new_text)
# if direction == "encode":
#     encrypt(t = text,s = shift)
# elif direction == "decode":
#     encrypt(t = text,s = -shift)
# else:
#     print("Please type 'encode or 'decode' ")
### In one function:
    
