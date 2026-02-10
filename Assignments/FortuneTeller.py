print("Hello user! I am a magical fortune teller")
try:
    Initiation=input("Would you like me to tell you your fortune?").strip().lower()
    if Initiation=="yes":
        print("That one experiement with the glowing cats ")
    if Initiation=="no":
        print("Oh... well that's too bad!")
        print("The fortune teller is sad now :(")
        quit()
except ValueError:
    print("Invalid input, try again!")
#Wait... its all strings?
#Always has been.
#else: commenting this for now because its breaking something
#This runs assuming the try part of the code works and this breaks the loop
#And continuing this absolutely god awful, no good, absolutely dreadful code
# #I was on 4 hours of sleep when i first wrote this, genuinely what does ANY of this mean