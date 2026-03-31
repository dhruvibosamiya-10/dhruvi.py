src=open("HELLO.TXT","r")
data=src.read()
src.close()

dst=open("HELLO.TXT","w")
dst.write(data)
dst.close()
print("file sucessfully copied ")
