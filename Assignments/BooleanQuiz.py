print("Answer all 5 questions with either 'True' or 'False")
#Answer key: 1=True 2=True 3=False 4=False 5=True
Question_1=input("George Boolean was a British mathematician: ")
if Question_1.lower()=="true":
    print("Correct") 
elif Question_1.lower()=="false":
    print("Incorrect") 
else:
    print("Invalid response, please answer with either 'True' or 'False'")

Question_2=input("Boolean expressions use 'True' or 'False': ")
if Question_2.lower()=="true":
    print("Correct")
elif Question_2.lower()=="false":
    print("Incorrect")
else:
    print("Invalid response, please answer with either 'True' or 'False'")


Question_3=input("A Boolean expression requires the data type to be in string format: ")
if Question_3.lower()=="false":
    print("Correct")
elif Question_3.lower()=="true":
    print("Incorrect")
else:
    print("Invalid response, please answer with either 'True' or 'False'")

Question_4=input("'=' is the comparison operator for 'Equal to': ")
if Question_4.lower()=="false":
    print("Correct")
elif Question_4.lower()=="true":
    print("Incorrect")
else:
    print("Invalid response, please answer with either 'True' or 'False'")


Question_5=input("The 'True' and 'False' are case sensitive: ")
if Question_5.lower()=="true":
    print("Correct")
elif Question_5.lower()=="false":
    print("Incorrect")
else:
    print("Invalid response, please answer with either 'True' or 'False'")