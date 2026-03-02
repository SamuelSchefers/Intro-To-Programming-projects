Fruits=["Banana","Orange","Apple","Pear","Melon", "Orange"]
print(Fruits[0])
print(Fruits[-1])
print(Fruits)
Fruits.append("Cherry")
print(Fruits)
Remove=input("What # fruit would you like to remove? ")
Fruits.pop(int(Remove))
print(Fruits)
Fruits.sort()
print (Fruits)
print(Fruits.count("Orange"))
for item in Fruits:
    print(item)