myfile= open("text.txt","r")
print(myfile.read())
print(myfile.readline(15))
for x in myfile:
    print("Line is:",x)
