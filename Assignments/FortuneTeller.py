import random
def question_1():
     print("What is your lucky number?")
def question_2():
    print("How many years into the future would you like to see?")
def question_3():
    print("Give me another magical number!")
#remember to int() and float() your question values, or else this piece of shitware will break
print("Hello user! I am a magical fortune teller")
def fortune_teller():
        Initiation=input("Would you like me to tell you your fortune?").strip().lower()
        if Initiation=="yes":
            print("Perfect! Allow me to ask you 3 simple questions and I shall determine your fortune!")
        elif Initiation=="no":
            print("Oh... well that's too bad!")
            print("The fortune teller is sad now :(")
            quit()
        else:
            print("Please answer with yes or no!")
            fortune_teller() #loops back if invalid input... im not using whatever try except bs for this when this works "perfectly" fine
fortune_teller() # Actually makes the function run
print("The experiment with the glowing cats") #yes im going to keep using this as a placeholder to tell when parts ot the code run correctly
#fun fact, there was an experiment with cat genetics where they were testing if cat genes were hereditary or not, and to test they glued bioluminescent genes to the cats genes they were testing and then if the kittens were glowing then they knew the genes were hereditary. The print function in with this line is a reference to that experiment because its how i tell if my code works.
#I was on 4 hours of sleep when i first wrote this, genuinely what does ANY of this mean
#writing the 5 possible fortunes here
#"I forsee a terrible accident at sea that leaves you and 3 others stranded on a deserted island forever, never to be rescued!"
#"I forsee a grand future full of love and happiness, and immense wealth beyond your wildest dreams!"
#"I am terribly sorry but I forsee a great swarm of locusts descending upon your land and devouring all of your crops, leaving you with nothing but a barren wasteland and a lifetime of regret"
#"I forsee a future where you will have immense wealth but will never find true love"
#"I forsee a mediocre life, with a stable job, a loving family, and a small house in the suburbs"

#remember that you can use the return function to return a value from a function, so you can use that in the randomizer