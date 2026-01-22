print("Answer all 5 questions with either 'True' or 'False'")
#Answer key: 1=True 2=True 3=False 4=False 5=True
Question_1=input("George Boolean was a British mathematician: ")
Question_1_bool=bool(Question_1)
Answer_1 = True
if Question_1_bool==True:
    print("Correct")
elif Question_1==False:
    print("Incorrect")
else:
    print("Invalid response, please answer with either 'True' or 'False'")

Question_2=input("Boolean expressions use 'True' or 'False': ")
Answer_2Bool=bool(Question_2)
if Answer_2Bool==True:
    print("Correct")
else:
    print("Incorrect")

Question_3=input("A Boolean expression requires the data type to be in string format: ")
Answer_3Bool=bool(Question_3)
if Answer_3Bool==False:
    print("Correct")
else:
    print("Incorrect")

Question_4=input("'=' is the comparison operator for 'Equal to': ")
Answer_4Bool=bool(Question_4)
if Answer_4Bool==False:
    print("Correct")
else:
    print("Incorrect")

Answer_5=input("The 'True' and 'False' are case sensitive: ")
Answer5_Bool=bool(Answer_5)
if Answer5_Bool==True:
    print("Correct")
else:
    print("Incorrect")