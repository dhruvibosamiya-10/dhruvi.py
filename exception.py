try:
    number1=int(input("Enter a number:"))
    number2=int(input("Enter another number:"))
    result=number1/number2

except ZeroDivisionError:
    print("you cannot divide by zero")

except ValueError:
    print("pless enter a valid number")

else:
    print("division sucessfully result is",result) 

finally:
    print("this block always run")    


try:
    my_list=[1,2,3]
    print(my_list[2])

except IndexError:
    print("index is out of range")

else:
    print("element found sucessfully")

finally:
    print("program finished")                   