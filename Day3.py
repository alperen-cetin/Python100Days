# #Challenge 1: even/odd number definer
# num = int(input("your number:"))
# if num == 2 or num % 2 == 0:
#     print("even num")
# elif num != 2 and num % 2 == 1:
#     print("num is odd")



# #Challenge 2: bmi calculator // Note: Course suggested me to use 
# # nested if statements but this way it's easier to read the code.
# height = float(input("your height: "))
# weight = float(input("your weight: "))

# bmi = round(weight/ (height ** 2),2)

# a = underWeight = bmi < 18.5
# b = normalWeight = bmi > 18.5 and bmi < 25
# c = overWeight = bmi > 25 and bmi < 30
# d = obese = bmi > 30 and bmi < 35
# e = clinicallyObese = bmi > 35

# if a is True:
#     print("Underweight")
# if b is True:
#     print("Normal weight")
# if c is True:
#     print("Overweight")
# if d is True:
#     print("Obese")
# if e is True:
#     print("Clinically obese")

# #Challenge 3: leap year calculator

# year = int(input("year: "))
# leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0 
# if leap == True:
#     print("Leap year")
# if leap == False: # else: 
#     print("Nope")

# #Challenge 4: Pizza Order // using nested if/else statements to see how hard the
# #code became to read
# print("Welcome!")
# size = input("What size pizza do you want? S, M, B\n")
# add_pepperoni = input("Do you want pepperoni? 'Y or N'\n")
# extra_cheese = input("Do you want extra cheese? 'Y or N'\n")

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "B":
#     bill += 25
# else:
#     print("undefined")   

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     elif size == "M" or "B":
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Bill is {bill}$")

#Challenge 5: Love Calculator
print("Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined = name1.lower() + name2.lower()
t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e = combined.count("e")
l = combined.count("l")
o = combined.count("o")
v = combined.count("v")
true = t + r + u + e
love = l + o + v + e 
scor = str(true) + str(love)
score = int(scor)
if score < 10 or score > 90:
    print("I don't know what am i doing with my life right now")
elif 40 > score < 50:
    print("Life is meaningles and we all are going to die")
else:
    print(f"your score is: {scor}")





        


    








    
