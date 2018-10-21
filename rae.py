userz = {}
userz["default1"] = "cumulative"
userz["INDRICK_BOREALE"] = "spessmahren"

a = input("Username: ")
b = input("Password: ")


if a in userz: #the "in" operator checks if the sequence has that item. True or False.
    if b == userz[a]:
        print("CREDENTIALS ACCEPTED")
    else:
        print("CREDENTIALS INVALID")
else:
    userz.update({a: b})
    print("ACCOUNT CREATED")


print(userz)