#Challenge1: Average height using for loops
student_heights = input("input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


# a = sum(student_heights)
# b = len(student_heights)
# print(a / b)
b = 0
c = 0
for a in student_heights:
    b += a
    c += 1
average_height = round(b/c)
print(average_height)

#Challenge2: Highest score
student_scores = input("input a list of scores").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])


b = 0
for a in student_scores:
    if a > b:
        b = a
print(f"highest score is: {b}")

#Challenge3: Sum of even numbers
a = 0
for i in range(2,101,2):
    a += i
print(a)

#Challenge4: FizzBuzz   

for num in range(1,101,1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#Challenge5: Password Creator
import random
txt = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['0','1','2','3','4','5','6','7','8','9']
sym = ['!','£','#','$','%','&','(',')','*','+']
print("My Password Generator")
letters = int(input("How many letters do you need in your password?\n"))
symbols = int(input("How many symbols do you need in your password?\n"))       
numbers = int(input("How many numbers do you need in your password?\n")) 

letters = random.choices(txt, k = letters)
symbols = random.choices(sym, k = symbols)
numbers = random.choices(num, k = numbers)
items = letters + symbols + numbers
random.shuffle(items)
str_x = ""
for item in items:
    str_x += item
print(str_x)




    
        


    

