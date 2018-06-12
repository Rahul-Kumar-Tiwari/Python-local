file= open("write.txt","w")
list=""
name=""
while(name !="xxx"):
    name=input("Name :")
    list += name
    list += ","
print("Saving",list)
file.write(list)
file.close()