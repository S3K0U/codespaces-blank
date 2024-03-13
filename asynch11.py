# Intro to Python Async Work
# Monday March 11th, 2024.

# INSTRUCTIONS
# Create a new python file called async_3_11.py
# Answer the following questions. Once you've completed the questions, commit
# and sync your work.
# This activity must be completed by the end of class in order to recieve
# a grade.

# REMEMBER - TAKE YOUR TIME AND DO YOUR BEST! DO NOT GIVE UP! 

# 1. Which Python datacasting function would
# you use if you wanted to convert a string data type
# into an integer data type? Please write your response
# in a complete sentence.   I would use Integer.parselent method because its an easy method to convert 
#a string into an integer data type.

# 2. Create a list called numbCol that contains three (3 ) colors and three (3) numbers.
#number ={"orange," "purple," "black," 1,2,3 }
# 3. You have been hired by a University to create
# a scholarship function. The client would like to provide 
# students a scholarship to their school based on the following
# conditions; 
# - If the user has never gotten a loan before and,
#-  if the user has never been to college before.
# The client would like you to use the logical NOT operator that will
# compare the condtions and return false. If the result is false, the client
# would also like the program to print the message "congrats! you've gotten the scholarship."
# the client has given you the choice on how to enter data for your function.
# you may enter data using input or pass in data into your function as parameters. 

def check_scholarship(has_loan, has_attended_college):
    if not has_loan and not has_attended_college:
        print("Congrats! You got the scholarship.")
    else:
        print("Sorry, you didnt get the scholarship.")

have_loan = input("Have you ever gotten a loan before? (yes/no)"