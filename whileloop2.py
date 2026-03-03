""" 1. Print numbers 1 to 5
i=1
while i<=5:
    print(i)
    i=i+1 """

""" 2. Sum of numbers take user input 
n=int(input("Enter Number : "))
i=1
s=0
while i<=n:
    s=s+i
    i=i+1
print("sum = ",s)  """  

""" 3. Print odd number between 1 to 20
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1 """

""" 4. Table of a Number 4
num=int(input("Enter Number : "))
i=1
while i<=10:
    print(num , " x " , i , " = " , num*i)
    i=i+1 """

""" 5. Print reverse number like 5 4 3 2 1 
i = 5
while i >= 1:
    print(i, end=" ")
    i -= 1   """

""" 6. Find largest number in list 
numbers = [5, 9, 2, 15, 7]
largest = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1
print("Largest number is:", largest)  """

""" 7. Print even numbers between 1 to 20 """
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1