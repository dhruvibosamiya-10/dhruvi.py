""" 1. Basic slices 
from array import array
arr = array('i',[10,20,30,40,50])
print(arr[1:4]) # index 1 to 3
print(arr[:3]) # start to index 2
print(arr[2:]) # index 2 to end
print(arr[:]) # entire array """

""" 2. Slicing with step 
from array import array
arr = array('i',[10,20,30,40,50,60,70,80])
print(arr[::2]) # every second elements
print(arr[::3]) # every third elements
print(arr[1::2]) # every second element starting from index 1 """

""" 3. Negative slicing 
from array import array
arr = array('i',[10,20,30,40,50])
print(arr[-4:-1]) # from index -4 to -2
print(arr[-3:]) # last third elements
print(arr[:-2]) # all except last two """

""" 4. Reverse array using slicing 
from array import array
arr = array('i',[10,20,30,40,50])
print(arr[::-1]) """

""" 5. Modifying slices """
from array import array
arr = array('i',[10,20,30,40,50])
arr[1:4] = array('i',[25,35,45])
print(arr) 
