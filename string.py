message="welcome to pythone a whole new world"
m2="5464"
print(str.capitalize(message))

print(message.center(60,'*'))
print(message.center(60,' '))
print(message.count('e'))
print(message.find('z'))
if message.find('z')==-1:
    print("No Match")
print(message.isalpha())
print(m2.isdigit())
print(len(message))