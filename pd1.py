1.
num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")
2.
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
3.
l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
else:
	print("%s is a consonant." % l)
4.
while True:
	print("Enter '0' for exit.")
	ch = input("Enter any character: ")
	if ch == '0':
		break
	else:
		if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
			print(ch, "is an alphabet.\n")
		else:
			print(ch, "is not an alphabet.\n")
5.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number between",num1,",",num2,"and",num3,"is",largest)
6.
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
7.
a=1
n=5
for a in range(n):
    print"hello" 
8.
num = int(input("Enter a number: "))
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)
9.
num = int(input("Enter a number: "))
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)
    
10.
Number = int(input("Please Enter any Number: "))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1
 
print("\n Number of Digits in a Given Number = %d" %Count)
11.
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))
12.
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
13.
num = int(input("Enter a number: "))


if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")
14.
lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
15.
lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for i in range(lower,upper+1):
    if not(i%2!=0):
        print(i)
16.
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
17.
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
18.
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):

   order = len(str(num))
    
   
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
19.
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
20.
num = int(input("Display multiplication table of: "))
for i in range(1, 11):
   print(num,'x',i,'=',num*i)
