Windspeed=input("Seems like a storm is blowing in! Please enter the wind speed of the storm to classify it: ")
print("You entered "+Windspeed+" MPH, if this is incorrect, please restart the program!")
if Windspeed<74:
    print("It's a tropical storm!")
elif Windspeed>=74 and Windspeed<96:
    print("It's a Category 1 hurricane!")
elif Windspeed>=96 and Windspeed<111:
    print("It's a Category 2 hurricane!")
elif Windspeed>=111 and Windspeed<130:
    print("It's a Category 3 hurricane!")
elif Windspeed>=130 and Windspeed<157:
    print("It's a Category 4 hurricane!")
else:
    print("ITS A CATEGORY 5 HURRICANE, TAKE SHELTER IMMEDIATELY!")
#Tropical storm < 74 MPH
#Category 1 < 96 MPH
#Category 2 < 111 MPH
#Category 3 < 130 MPH
#Category 4 < 157 MPH
#Category 5 >=157 MPH