"""
UCS420: Cognitive Computing
Assignment 1 - Learn Python
16 programs covering: Syntax, Loops, if-else, Data Structures, Strings,
File Handling, Exception Handling, Random Numbers, Command Line Arguments,
and Use of Libraries.

Name   : Aarav
Roll No: 1024160106
Branch : CSE

Note: Sections that normally take input() (2.3 style user input, file
name prompts, etc.) are kept as input() calls so this can be run and
demoed exactly like the original Colab notebook. Run with:
    python3 assignment1_learn_python.py
"""

import math as m
import random as r
import string as s
import sys


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------
section("1. Hello World")
# ---------------------------------------------------------------------
print("Hello World")

# Assignment 1.1: WAP to print your name three times
for _ in range(3):
    print("Aarav")


# ---------------------------------------------------------------------
section("2. Add numbers and Concatenate strings")
# ---------------------------------------------------------------------
# 2.1 Add two numbers
a = 10
b = 220
c = a + b
print(a, " + ", b, " --> ", c)

# 2.2 Concatenate two strings
a = "Bhagat"
b = " Singh"
c = a + b
print(a, " + ", b, " --> ", c)

# 2.3 Concatenate string with number
a = "Bhagat"
b = 100
c = a + str(b)
print(a, " + ", b, " --> ", c)

# Assignment 2.1: WAP to add three numbers and print the result
n1, n2, n3 = 5, 15, 25
print("Sum of three numbers -->", n1 + n2 + n3)

# Assignment 2.2: WAP to concatenate three strings and print the result
s1, s2, s3 = "Cognitive", " ", "Computing"
print("Concatenated string -->", s1 + s2 + s3)


# ---------------------------------------------------------------------
section("3. Input from user")
# ---------------------------------------------------------------------
# 3.1 Input two strings from user and concatenate them
a = input("Enter First String: ")
b = input("Enter Second String: ")
c = a + b
print(a, " + ", b, "      --> ", c)

# 3.2 Input two numbers from user and add them
a = int(input("Enter First No: "))
b = int(input("Enter Second No: "))
c = a + b
print(a, " + ", b, " --> ", c)


# ---------------------------------------------------------------------
section("4. Loop")
# ---------------------------------------------------------------------
# 4.1 While Loop
i = 1
while i <= 10:
    print(i)
    i = i + 1

# 4.2 Range Function
print("range(10)        --> ", list(range(10)))
print("range(10,20)     --> ", list(range(10, 20)))
print("range(0,20,2)    --> ", list(range(2, 20, 2)))
print("range(-10,-20,2) --> ", list(range(-10, -20, 2)))
print("range(-10,-20,-2)--> ", list(range(-10, -20, -2)))

# 4.3.1 For loop - Version 1
for i in range(0, 10):
    print(i)

# 4.3.2 For loop - Version 2
for i in range(0, 20, 2):
    print(i)

# 4.3.3 For loop - Version 3
for i in range(0, -10, -1):
    print(i)

# 4.4 Print table of 5
for i in range(1, 11):
    print(5, " * ", i, " = ", i * 5)

# 4.5.1 Sum all numbers from 1 to 10 - Version 1
sum_v1 = 0
for i in range(1, 11):
    sum_v1 = sum_v1 + i
print("Sum is --> ", sum_v1)

# 4.5.2 Sum all numbers from 1 to 10 - Version 2
print("Sum is --> ", sum(range(1, 11)))

# Assignment 4.1: WAP to print the table of 7, 9
for table in (7, 9):
    for i in range(1, 11):
        print(table, " * ", i, " = ", table * i)

# Assignment 4.2: WAP to print the table of n (n given by user)
n = int(input("Enter n for its multiplication table: "))
for i in range(1, 11):
    print(n, " * ", i, " = ", n * i)

# Assignment 4.3: WAP to add all numbers from 1 to n (n given by user)
n = int(input("Enter n to sum 1 to n: "))
print(f"Sum from 1 to {n} --> ", sum(range(1, n + 1)))


# ---------------------------------------------------------------------
section("5. If-Else - Conditional Checking")
# ---------------------------------------------------------------------
# 5.1 Input two numbers from user and compare them
a = int(input("Enter First No: "))
b = int(input("Enter Second No: "))
if a > b:
    print(a, " > ", b)
else:
    print(a, " < ", b)

# 5.2 Check whether a number is odd or even
n = int(input("Enter a No: "))
if n % 2 == 0:
    print(n, " is even")
else:
    print(n, " is odd")

# 5.3 Check whether a number is prime or not
n = int(input("Enter a No: "))
f = 0
for i in range(2, n // 2 + 1):
    if n % i == 0:
        f = 1
        break
if f == 0:
    print("Prime")
else:
    print("Not Prime")

# 5.4 Conditional Checking - Compare strings
a = input("Enter First String : ")
b = input("Enter Second String: ")
if a == b:
    print("a == b")
elif a >= b:
    print("a > b")
else:
    print("a < b")

# Assignment 5.1: WAP to find max among three numbers, input from user
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
print("Max --> ", max(n1, n2, n3))

# Assignment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n
n = int(input("Enter n: "))
total = sum(x for x in range(1, n + 1) if x % 7 == 0 and x % 9 == 0)
print(f"Sum of numbers divisible by 7 and 9 from 1 to {n} --> ", total)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


# Assignment 5.3: WAP to add all prime numbers from 1 to n
n = int(input("Enter n: "))
prime_sum = sum(x for x in range(1, n + 1) if is_prime(x))
print(f"Sum of prime numbers from 1 to {n} --> ", prime_sum)


# ---------------------------------------------------------------------
section("6. Functions")
# ---------------------------------------------------------------------
# 6.1 Add two numbers
def Add(a, b):
    c = a + b
    return c


print("Add(10,20) -->", Add(10, 20))
print("Add(20,50) -->", Add(20, 50))
print("Add(80,200) -->", Add(80, 200))


# 6.2 Prime number
def IsPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return 1


print("IsPrime(20)  --> ", IsPrime(20))
print("IsPrime(23)  --> ", IsPrime(23))
print("IsPrime(200) --> ", IsPrime(200))
print("IsPrime(37)  --> ", IsPrime(37))


# 6.3 Add 1 to n
def AddN(n):
    return sum(range(n + 1))


print("AddN(10)  --> ", AddN(10))
print("AddN(20)  --> ", AddN(20))
print("AddN(50)  --> ", AddN(50))
print("AddN(200) --> ", AddN(200))


# Assignment 6.1: WAP using function that adds all odd numbers from 1 to n
def AddOdd(n):
    return sum(x for x in range(1, n + 1) if x % 2 != 0)


n = int(input("Enter n: "))
print(f"Sum of odd numbers from 1 to {n} --> ", AddOdd(n))


# Assignment 6.2: WAP using function that adds all prime numbers from 1 to n
def AddPrimes(n):
    return sum(x for x in range(1, n + 1) if IsPrime(x))


n = int(input("Enter n: "))
print(f"Sum of prime numbers from 1 to {n} --> ", AddPrimes(n))


# ---------------------------------------------------------------------
section("7. Math library")
# ---------------------------------------------------------------------
print("exp(-200)    --> ", m.exp(-200))
print("log(100,2)   --> ", m.log(100, 2))
print("log(100,10)  --> ", m.log(100, 10))
print("log10(100)   --> ", m.log10(100))
print("m.cos(30)    --> ", m.cos(30))
print("m.sin(30)    --> ", m.sin(30))
print("m.tan(30)    --> ", m.tan(30))
print("m.sqrt(324)  --> ", m.sqrt(324))
print("m.ceil(89.9) --> ", m.ceil(89.9))
print("m.floor(89.9)--> ", m.floor(89.9))


# ---------------------------------------------------------------------
section("8. Strings")
# ---------------------------------------------------------------------
# 8.1 Indexing in string
var = "Hello World!"
print("var      --> ", var)
print("var[0]   --> ", var[0])
print("var[1:5] --> ", var[1:5])
print("var[:-5] --> ", var[:-5])

# 8.2 String length, upper, lower
var = "Hello World!"
print("String --> ", var)
print("Length --> : ", len(var))
print("Upper  --> : ", var.upper())
print("Lower  --> : ", var.lower())

# 8.3 String formatting
name = input("Enter your name: ")
age = int(input("Enter your age : "))
price = float(input("Enter the book price: "))
out = "\nYour name is %s, age is %d and book price is %f" % (
    name.upper(), age, price)
print(out)

# 8.4 String in Triple Quotes
para_str = """This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)

# 8.5 String strip
var = " Indian   Army    "
print("String    --> ", var)
print("Length    --> ", len(var))
print("var strip --> ", var.strip())
print("Length of var after strip --> ", len(var.strip()))

# 8.6 String split
var = " Indian,   Army    "
print("String    --> ", var)
print("Length    --> ", len(var))
print("var split --> ", var.split())
print("var split --> ", var.split(' '))
print("var split --> ", var.split(','))
print("var split --> ", var.strip().split(','))

# 8.7 Count in string
var = " Indian Army    "
print("String       --> ", var)
print("Count of ' ' --> ", var.count(' '))
print("Count of 'a' --> ", var.count('a'))
print("Count of 'n' --> ", var.count('an'))

# 8.8 Reverse a String
var = "Indian Army"
print("String    --> ", var)
print("var[::1]  --> ", var[::1])
print("var[::2]  --> ", var[::2])
print("var[::-1] --> ", var[::-1])
print("var[::-2] --> ", var[::-2])
var = var[::-1]
print("var after reverse --> ", var)

# 8.9 Palindrome
s1 = "Indian Army"
s2 = "malayalam"
s3 = "madam"
s4 = "teacher"
print("s1 --> ", s1 == s1[::-1])
print("s2 --> ", s2 == s2[::-1])
print("s3 --> ", s3 == s3[::-1])
print("s4 --> ", s4 == s4[::-1])


# ---------------------------------------------------------------------
section("9. Random Numbers/String")
# ---------------------------------------------------------------------
# 9.1 Generate random number between 0 and 1
print(r.random())
print(r.random())
print(round(r.random(), 4))

# 9.2 Generate random integer number
print(r.randint(1, 100))
print(r.randint(1, 100))
print(r.randint(-10, 10))
print(r.randint(-10, 10))

# 9.3 Generate random real number
print(r.uniform(1, 100))
print(r.uniform(1, 100))
print(r.uniform(-10, 10))
print(r.uniform(-10, 10))
print(round(r.uniform(-10, 10), 2))

# 9.4 Select sample from a list of elements
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(r.sample(A, 4))
print(r.sample(A, 2))
print(r.sample(range(0, 100), 2))
print(r.sample(range(-100, 100), 5))

# 9.5 Generate random string
print("String        --> ", s.ascii_letters)
passwd = r.sample(s.ascii_letters, 6)
print("Selected Char --> ", passwd)
passwd1 = "".join(passwd)
print("passwd1       --> ", passwd1)
passwd2 = "+".join(passwd)
print("passwd2       --> ", passwd2)
passwd3 = "*".join(passwd)
print("passwd3       --> ", passwd3)

# 9.6 Generate random digits
print("Digits --> ", s.digits)
otp = r.sample(s.digits, 5)
print("Selected num1 --> ", otp)
otp = "".join(otp)
print("otp1          --> ", otp)
otp = r.sample(s.digits, 5)
print("Selected num2 --> ", otp)
otp = "".join(otp)
print("otp2          --> ", otp)
otp = r.sample(s.digits, 5)
print("Selected num2 --> ", otp)
otp = "".join(otp)
print("otp3          --> ", otp)

# 9.7 Generate random string + digits
print("String + Digits --> ", s.ascii_letters + s.digits)
mixPasswd = r.sample(s.ascii_letters + s.digits, 5)
print("\nSelected Str1 --> ", mixPasswd)
mixPasswd = "".join(mixPasswd)
print("mixPasswd1    --> ", mixPasswd)

mixPasswd = r.sample(s.ascii_letters + s.digits, 6)
print("\nSelected Str2 --> ", mixPasswd)
mixPasswd = "".join(mixPasswd)
print("mixPasswd2    --> ", mixPasswd)

splChar = "#@!~%^&*()_+=-[]{}|"
mixPasswd = r.sample(splChar + s.ascii_letters + s.digits, 8)
print("\nSelected Str3 --> ", mixPasswd)
mixPasswd = "".join(mixPasswd)
print("mixPasswd3    --> ", mixPasswd)


# ---------------------------------------------------------------------
section("10. Exception Handling")
# ---------------------------------------------------------------------
# 10.2 Exception handling for division by zero
for i in range(-5, 6):
    try:
        print("100/", i, " --> ", 100 / i)
    except ZeroDivisionError:
        print("error")

# 10.3 Exception handling for array out of index
L_ex = [1, 2, 3, 4, 5]
for i in range(8):
    try:
        print(i, " --> ", L_ex[i])
    except IndexError:
        print("error")

# 10.5 Exception handling for file not found
fileName = input("Enter File Name: ")
try:
    fp = open(fileName)
    fp.close()
except FileNotFoundError:
    print("Error !! \"%s\" File Not Found" % (fileName))
print("Done")


# ---------------------------------------------------------------------
section("11. Data Structure 1 - List")
# ---------------------------------------------------------------------
L = ["Pratham", 'Sharma', 3.14, 3]
print("Original List: ", L)
print("Number of elements in list: ", len(L))

i = 0
while i < len(L):
    print(L[i])
    i += 1

for i in range(0, len(L)):
    print(L[i])

for s_ in L:
    print(s_)

L = ["Pratham", 'Sharma', 3.14, 3]
print("Original List       --> ", L)
L.append("Rahul")
print("List After Adding   --> ", L)
del L[1]
print("List After Deleting --> ", L)

L = [3, 6, 9, 12, 5, 3, 2]
print("Original List --> ", L)
print("Sum     --> ", sum(L))
print("Average --> ", sum(L) / len(L))
print("Average --> ", sum(L) // len(L))
print("L * 3   --> ", L * 3)
print("L + L   --> ", L + L)

print("max --> ", max(L))
print("min --> ", min(L))
L.sort()
print("After Sort (Ascending)  --> ", L)
L.sort(reverse=True)
print("After Sort (Descending) --> ", L)

L1 = [3, 6, 9]
L2 = [12, 5, 3, 2]
L3 = L1 + L2
print("L3[2:]  --> ", L3[2:])
print("L3[2:5] --> ", L3[2:5])
print("L3[:-1] --> ", L3[:-1])
print("L3[::2] --> ", L3[::2])

L = [12, 5, 3, 2, 7]
newL = [i * 5 for i in L]
print("After Multiply with constant --> ", newL)

L = [3, 6, 9, 12, 5, 3, 2]
print("6 in L --> ", 6 in L)
print("10 in L --> ", 10 in L)


# ---------------------------------------------------------------------
section("12. Data Structure 2 - Dictionary")
# ---------------------------------------------------------------------
CGPA = {1: 8.9, 2: 5.6, 4: 6.7, 7: 9.1, 8: 5.3}
for k in CGPA:
    print("CGPA of ", k, " --> ", CGPA[k])

print("Keys   --> ", list(CGPA.keys()))
print("Values --> ", list(CGPA.values()))

CGPA[4] = 9.2
CGPA[3] = 8.6
del CGPA[1]
print("After updates --> ", CGPA)

print("Is Key 2 Present --> ", 2 in CGPA)
print("Is Key 9 Present --> ", 9 in CGPA)

HomeTown = {"Prashant": "Delhi", "Govind": "Gwalior",
            "Anil": "Morena", "Pankaj": "Agra"}
for d in HomeTown:
    print("Home Town of ", d, " is  --> ", HomeTown[d])


# ---------------------------------------------------------------------
section("13. Data Structure 3 - Tuple")
# ---------------------------------------------------------------------
T = ("Pratham", 'Sharma', 3.14, 3)
print("T --> ", T, " Type --> ", type(T))

T = (3, 6, 9, 12, 5, 3, 2)
print("T[1:3]   --> ", T[1:3])
print("T[-4:-1] --> ", T[-4:-1])
print("Sum --> ", sum(T), " Average --> ", sum(T) / len(T))
print("Max --> ", max(T), " Min --> ", min(T))

T1 = (3, 6, 9)
T2 = (12, 5, 3, 2)
print("T1 + T2 --> ", T1 + T2)

# Adding/inserting/deleting via list conversion ("jugaad")
T = ("Pratham", 'Sharma', 3.14, 3)
T1 = list(T)
T1.append(9.8)
T = tuple(T1)
print("After Add --> ", T)

T = ("Pratham", 'Sharma', 3.14, 3)
T1 = list(T)
T1.insert(2, "Rahul")
T = tuple(T1)
print("After Insert --> ", T)

T = ("Pratham", 'Sharma', 3.14, 3)
T1 = list(T)
del T1[1]
T = tuple(T1)
print("After Delete --> ", T)


# ---------------------------------------------------------------------
section("14. Data Structure 4 - Set")
# ---------------------------------------------------------------------
set1 = set(['A', 'B', 'E', 'F', 'E', 'F'])
print("Original set --> ", set1, " Num of elements --> ", len(set1))

a_set = set(['A', 'B', 'E', 'F'])
b_set = set(["A", "C", "D", "E"])
print("Union            --> ", a_set.union(b_set))
print("Intersection     --> ", a_set.intersection(b_set))
print("Difference a - b --> ", a_set.difference(b_set))
print("Difference b - a --> ", b_set.difference(a_set))
print("Symmetric diff   --> ", a_set.symmetric_difference(b_set))

a_set.add("D")
print("After adding D --> ", a_set)
a_set.remove("D")
print("After removing D --> ", a_set)
a_set.pop()
print("After pop --> ", a_set)


# ---------------------------------------------------------------------
section("15. Command Line Argument")
# ---------------------------------------------------------------------
# Note: run these interactively at the command line, e.g.:
#   python3 assignment1_learn_python.py 10 20
print(sys.argv)
if len(sys.argv) >= 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a, " + ", b, " --> ", a + b)

total_cli = 0
for arg in sys.argv[1:]:
    try:
        total_cli += int(arg)
    except ValueError:
        pass
print("Sum of numeric cmd-line args --> ", total_cli)


# ---------------------------------------------------------------------
section("16. File Handling")
# ---------------------------------------------------------------------
# 16.1 Writing 1 to 10 in file
fp = open('result.txt', 'w')
for i in range(1, 11):
    fp.write(str(i) + "\n")
fp.close()
print("Writing done !! \nOpen result.txt to view the content")

# 16.2 Read a file and print its content
fp = open('result.txt')
for line in fp:
    print(line.strip())
fp.close()

# 16.3 Read from one file, convert to upper case, write to another file
Readfp = open('result.txt')
Writefp = open('abc.txt', 'w')
for line in Readfp:
    Writefp.write(line.upper())
Writefp.close()
Readfp.close()
print("Writing done !! \nOpen abc.txt to view the content")
