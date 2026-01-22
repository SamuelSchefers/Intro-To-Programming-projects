# 1. Define the question and the correct answer
question = "The sun rises in the west. True or False? "
correct_answer = False

# 2. Ask the user for their input
# Convert input to lowercase to handle various input styles (e.g., "True", "true")
user_input = input(question).strip().lower()

# 3. Determine if the user's answer is correct
# We need to map the string input "true" or "false" to the actual boolean values True or False
if user_input == "true":
    user_answer = True
elif user_input == "false":
    user_answer = False
else:
    # Handle invalid input gracefully
    print("Invalid input. Please answer 'True' or 'False'.")
    user_answer = None # Set to None to indicate an error

# 4. Provide feedback based on the result
if user_answer is not None:
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is {correct_answer}.")