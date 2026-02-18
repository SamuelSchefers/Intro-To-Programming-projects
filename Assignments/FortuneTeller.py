import random
def question_1():
    Answer1=(input("What is your lucky number? "))
    try:
        float(Answer1)
    except TypeError:
        print("TypeError, Please enter a valid number.")
    except ValueError:
        print("Value error, Please enter a number. ")
    else:
        print("Else part test")
        str(Answer1) #Remove this line, was using it 
        #to test if it would allow me to print the answer from this function
        #it didnt.
        #We're just going to pretend it isnt an issue right now
        return Answer1
def question_2():
    Answer2=float(input("How many years into the future would you like to see? "))
def question_3():
    Answer3=float(input("Give me another magical number! "))
#remember to int() and float() your question values, or else this piece of shitware will break
print("Hello user! I am a magical fortune teller")
def fortune_teller():
        Initiation=input("Would you like me to tell you your fortune? ").strip().lower()
        if Initiation=="yes":
            print("Perfect! Allow me to ask you 3 simple questions and I shall determine your fortune!")
            return Initiation
        elif Initiation=="no":
            print("Oh... well that's too bad!")
            quit()
        else:
            print("Please answer with yes or no!")
            fortune_teller() #loops back if invalid input... works somehow
fortune_teller() # Actually makes the function run
print("The experiment with the glowing cats") #yes im going to keep using this as a placeholder to tell when parts ot the code run correctly
question_1()
print(question_1)
#writing the 5 possible fortunes here
#"I forsee a terrible accident at sea that leaves you and 3 others stranded on a deserted island forever, never to be rescued!"
#"I forsee a grand future full of love and happiness, and immense wealth beyond your wildest dreams!"
#"I am terribly sorry but I forsee a great swarm of locusts descending upon your land and devouring all of your crops, leaving you with nothing but a barren wasteland and a lifetime of regret"
#"I forsee a future where you will have immense wealth but will never find true love"
#"I forsee a mediocre life, with a stable job, a loving family, and a small house in the suburbs"

#remember that you can use the return function to return a value from a function, so you can use that in the randomizer