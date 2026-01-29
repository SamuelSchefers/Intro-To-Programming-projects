total_score=0
def score_counter():
    global total_score
    total_score+=1
question_1=input("What is the movie that came out in 2001 and stars an ogre and a donkey as its main characters?: ") #shrek
if question_1.lower()=="shrek":
    print("Correct!")
    score_counter()
else:
    print("Incorrect!")
question_2=input("What is the capital of Canada?: ") #ottawa
if question_2.lower()=="ottawa":
    print("Correct!")
    score_counter()
else:
    print("Incorrect!")
question_3=input("What material are most soda cans made of?: ") #aluminum
if question_3.lower()=="aluminum":
    print("Correct!")
    score_counter()
else:
    print("Incorrect!")
question_4=input("What is the 10th letter of the alphabet?: ") #j
if question_4.lower()=="j":
    print("Correct!")
    score_counter()
else:
    print("Incorrect!")
question_5=input("What organelle is considered to be the powerhouse of the cell?: ") #mitochondria
if question_5.lower()=="mitochondria":
    print("Correct!")
    score_counter()
else:
    print("Incorrect!")
question_6=input("What is the 7th month in a year?: ") #july
if question_6.lower()=="july":
    print("Correct!")
    score_counter()
else:
    print("Incorrect!")
#hardest part of this assignment is coming up with questions because im suuper creative
print("Your final score is " + str(total_score) + "/6")
if total_score==6:
    print("A perfect score! Great job!")
#test_variable=input("a:")
#if test_variable.lower()=="a":
#    total_score += 1
#else:
#    print("How did you already manage to mess up your code")
#print (total_score)