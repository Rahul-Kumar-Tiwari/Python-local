statement = "White dear fox jumnp over the cow yep thats it"
for letter in statement:

    if letter == "j":
        break
    print("Current letter", letter)
for letter in statement:
    if letter == "i":
       continue
    print("Current letter",letter)