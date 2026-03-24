# 1. Basic default arguments 
def greet(name,msg="GOOD MORNING"):
    print("HELLO",name + ",",msg)

greet("ASHA")
greet("RAVI","GOOD MORNING") 

# 2. Power Function 
def power(num,exp=2):
    return num**exp

print(power(3))    # uses default exp=2
print(power(3,3))  # overrides default
print(power(2,4))  

# 3. Multiple default arguments 
def student_info(name,age=18,course="BCA"):
    print("NAME : ",name)
    print("AGE : ",age)
    print("COURSE : ",course)

student_info("RAVI")
student_info("SEEMA",20)
student_info("AMIT",19,"BSC IT")    