""" 1. Integer array 
from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr)) """

""" 2. len() = number of elements 
from array import array
arr=array('i',[10,20,30,40,50])
print(len(arr)) """

""" 3. append(x) = add element at end             
from array import array
arr=array('i',[10,20,30,40])
arr.append(40)
print(arr) """

""" 4. insert(pos,x) = insert at position
from array import array
arr=array('i',[10,20,30])
arr.insert(2,40)
print(arr) """

""" 5. remove(x) = remove first occurence
from array import array
arr=array('i',[10,20,30])
arr.remove(20)
print(arr) """

""" 6. pop() = remove and return last element 
from array import array
arr=array('i',[10,20,30,40])
x = arr.pop()
print ("remove : " , x )
print(arr) """

""" 7. index(x) = find index of element 
from array import array
arr = array('i',[10,20,30,40])
print(arr.index(30)) """

""" 8. count(x) = count occurence 
from array import array
arr = array('i',[10,20,30,20,40])
print(arr.index(20)) """

""" 9. reverse() = reverse array """
from array import array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)