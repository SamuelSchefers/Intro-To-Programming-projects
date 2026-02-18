import random
def question_1():
    Answer1=(input("What is your lucky number? "))
    try:
        float(Answer1)
    except TypeError: #This just didnt ever come up for some reason, idk what it does tbh
        print("TypeError, Please enter a valid number!")
        question_1()
    except ValueError:
        print("Value error, Please enter a number!") #Error shows up when you answer the question as a not number
        question_1() #Loops function back
    else:
        #breaks loop when the answer is valid, returns it and hopefully doesnt break stuff?
        return Answer1
def question_2():
    Answer2=(input("How many years into the future would you like to see? "))
    try:
        float(Answer2)
    except ValueError:
        print("Value error, Please enter a number!")
        question_2()
    else:
        return Answer2
def question_3():
    Answer3=(input("Give me another magical number! "))
    try:
        float (Answer3)
    except ValueError:
        print("Value error, Please enter a valid number!")
        question_3()
    else:
        return Answer3
#remember to int() and float() your question values
print("Hello user! I am a magical fortune teller")
def fortune_teller():
        Initiation=input("Would you like me to tell you your fortune? ").strip().lower()
        if Initiation=="yes":
            print("Perfect! Allow me to ask you 3 simple questions and I shall determine your fortune!")
        elif Initiation=="no":
            print("Oh... well that's too bad!")
            quit()
        else:
            print("Please answer with yes or no!")
            fortune_teller() #loops back if invalid input... works somehow
fortune_teller() # Actually makes the function run
print("The experiment with the glowing cats") #yes im going to keep using this as a placeholder to tell when parts ot the code run correctly
question_1()
question_2()
question_3()
#writing the 5 possible fortunes here
#"I forsee a terrible accident at sea that leaves you and 3 others stranded on a deserted island forever, never to be rescued!"
#"I forsee a grand future full of love and happiness, and immense wealth beyond your wildest dreams!"
#"I am terribly sorry but I forsee a great swarm of locusts descending upon your land and devouring all of your crops, leaving you with nothing but a barren wasteland and a lifetime of regret"
#"I forsee a future where you will have immense wealth but will never find true love"
#"I forsee a mediocre life, with a stable job, a loving family, and a small house in the suburbs"

#remember that you can use the return function to return a value from a function, so you can use that in the randomizer