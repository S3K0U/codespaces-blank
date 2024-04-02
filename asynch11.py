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
#a string into an integer data type. Iwould use the int() data casting function. This function converts Anything passed inside of it into a interger number.

# 2. Create a list called numbCol that contains three (3 ) colors and three (3) numbers.
#numbCol =["orange," "purple," "black," 1,2,3 ]
[]#Curly- These brackets are used for objects.
{}#Square- These brackets are used for lists.
()#Round- These brackets are used for functions

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

#def check_scholarship(has_loan, has_attended_college):
   # if not has_loan and not has_attended_college:
      #  print("Congrats! You got the scholarship.")
  #  else:
        #print("Sorry, you didnt get the scholarship.")

#have_loan = input("Have you ever gotten a loan before? (yes/no)"

 def Scholarship(UserLoan, beenToCollege):   
     userLoan = input('Have you ever gotten a loan for school; True or False'):
     beenToCollege = input('Have you ever been to college before; True or False'):
     if not (userLoan == True and beenToCollege == True):
        print('Congrats youve gotten the scholarship!')
    elif userLoan== True and beenToCollege == False:
              print('Sorry, unfortunately you do not qualify for the Scholarship')
    elif userLoan== False and beenToCollege == True :
        else:
        print('Sorry, unfortunately you dont qualify for the scholarship')

Scholarship(False, False)
