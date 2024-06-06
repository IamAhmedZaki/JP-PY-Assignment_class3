# Write a program to check whether a person is eligible to vote or not?
# person=int(input("ENTER AGE:"))

# if person >= 18:
#     print("Person is eligible to vote !")
# else:
#     print("person is not eligble to vote")

# Write a program to check char is vowel or not.

# char=input("ENTER ALPHABET: ")
# char_2= char.upper()

# if char_2=="A" or char_2=="I" or char_2=="O" or char_2=="U" or char_2=="E":
#     print("Alphabet is Vowel")
# else:
#     print("Alphabet is not a Vowel")

# Write a program to check the number is positive or negative. User input.

# num=int(input("ENTER NUMBER: "))

# if num <=0:
#     print("Number is Negative")
# else:
#     print("Number is Positive")

# Write a program to check whether a number is odd or even?

# num=int(input("ENTER NUMBER: "))

# if num % 2 == 0:
#     print("Number is EVEN")
# else:
#     print("Number is ODD")

# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100

# user=int(input("Enter obtained marks: "))
# if user < 60:
#     print("Grade : F")
# elif user < 70:
#     print("Grade : D")
# elif user <= 80:
#     print("Grade : C")
# elif user < 90:
#     print("Grade : B")
# elif user >= 90:
#     print("Grade : A")

# Write a program to check whether a number is divisible by 7

# num=int(input("Enter number: "))
# if num % 7 == 0:
#     print("Divisible by 7")
# else:
#     print("Not divisible by 7")

# Write a program to check if year is leap year.
# NOTE: search on google of what leap year is.

# year= int(input("Enter Year: "))
# if year % 4 == 0:
#     print(str(year)+" is a leap year")
# else:
#     print(str(year)+" is not a leap year")

# Write a program to ask user its name and check whether name consists of 5 or more letters
# Name= input("Enter name: ")
# nameLen= len(Name)
# if nameLen > 5:
#     print ("name has more letters than 5")
# else:
#     print("name has 5 or less than 5 letters")


# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. 
# Perform operation accordingly
# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15
# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50
# input1=float(input("Enter 1st number: "))
# input2=float(input("Enter 2nd number: "))
# input3=input("Enter operator: ")
# if input3 == "*":
#     print(input1 * input2)
# elif input3 == "/":
#     print(input1 / input2)
# elif input3 == "+":
#     print(input1 + input2)
# elif input3 == "*":
#     print(input1 - input2)
# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# for example

# input1 is 10
# output should be "10 is only divisible by 2"
# input1 is 9
# output should be "9 is only divisible by 3"
# input1 is 12
# output should be "12 is divisible by 2 and 3"

# input1=int(input("Enter number:"))
# if input1 % 2 == 0 and input1 % 3 == 0:
#     print("Number is divisible by both 2 and 3")
# elif input1 % 2 == 0:
#     print("Number is only divisible by 2" )
# elif input1 % 3 == 0:
#     print("Number is only divisible by 3" )   


# Write a program that accepts 2 inputs from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5

# input1= int(input("Enter 1st number: "))
# input2= int(input("Enter 2nd number: "))

# if input1 > input2 :
#     print(str(input1)+" is larger")
# elif input2 > input1 :
#     print(str(input2)+ " is larger")


# Write a program that accepts 3 input from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 15 as this number is larger than 5 and 10

# input1= int(input("Enter 1st number: "))
# input2= int(input("Enter 2nd number: "))
# input3= int(input("Enter 3rd number: "))

# if input1 >input2 and input1>input3:
#     print(str(input1)+" is larger")
# elif input2 >input1 and input2>input3:
#     print(str(input2)+ " is larger")
# elif input3>input1 and input3>input2:
#     print(str(input3)+ " is larger")


# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15

# input1= int(input("Enter 1st number: "))
# input2= int(input("Enter 2nd number: "))
# input3= int(input("Enter 3rd number: "))

# if (input1>input2 and input1<input3) or (input1<input2 and input1>input3):
#     print(str(input1)+" is 2nd largest")
# elif (input2 >input1 and input2<input3)or(input2<input1 and input2>input3):
#     print(str(input2)+ " is 2nd largest")
# else:
#     print(str(input3)+ " is 2nd largest")

# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input
# Light=input("Enter Light Color: ")
# Light2= Light.upper()

# if Light2 == "YELLOW":
#     print("Car has to wait")
# elif Light2 == "GREEN":
#     print("Car is allowed to go")
# elif Light2 == "RED":
#     print("Car has to stop")
# else:
#     print("Wrong Input")
# 
# Write a program that takes two numbers as input and prints:

# "First number is greater" if the first number is greater than the second number.
# "Second number is greater" if the second number is greater than the first number.
# "Both numbers are equal" if the two numbers are equal.
# 
# input1= int(input("Enter 1st number: "))
# input2= int(input("Enter 2nd number: "))

# if input1 > input2 :
#     print("First number is greater")
# elif input2 > input1 :
#     print("Second number is greater")
# elif input2 == input1 :
#     print("Both numers are equal")

# 
# Write a program that takes a password as input and checks its strength:

# If the password length is less than 6, print "Weak password".
# If the password length is between 6 and 12, print "Moderate password".
# If the password length is more than 12, print "Strong password".

# input1= input("Enter 1st number: ")
# input2= len(input1)

# if input2 < 6:
#     print("Weak password")
# elif input2 >= 6 and input2 <= 12:
#     print("Moderate password")
# elif input > 12:
#     print("Strong Password")


# 
# Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

# If the years of service are less than 5, no bonus.
# If the years of service are between 5 and 10, bonus is 10% of the salary.
# If the years of service are more than 10, bonus is 20% of the salary.
# Print the bonus amount.

# employee_salary= float(input("Enter Salary: "))
# employee_years= int(input("Enter Years: "))


# if employee_years >= 5 and employee_years <= 10 :
#     employee_salary= employee_salary + (10*employee_salary)/100
# elif employee_years > 10:
#     employee_salary= employee_salary + (20*employee_salary)/100
# else:
#     print("No bonus")
# print(employee_salary)

# 
# Write a program that takes the total amount of a purchase as input and applies a discount:

# If the amount is less than $100, no discount.
# If the amount is between $100 and $500, apply a 10% discount.
# If the amount is more than $500, apply a 20% discount.
# Print the final amount after the discount.
# total_purchase= float(input("Enter Bill: "))



# if total_purchase >=  100 and total_purchase <= 500 :
#     total_purchase= total_purchase - (10*total_purchase)/100
# elif total_purchase > 500:
#     total_purchase= total_purchase - (20*total_purchase)/100
# elif total_purchase <  100:
#     print("No DISCOUNT")
# print(total_purchase)



# 
# Write a program that takes a person's age as input and prints the age group they belong to:

# If the age is less than 13, print "Child".
# If the age is between 13 and 19 (inclusive), print "Teenager".
# If the age is 20 or above:
#     If the age is less than 65, print "Adult".
#     If the age is 65 or above, print "Senior".


# age= int(input("Enter Age: "))


# if age < 13:
#     print("Child")
# elif age >= 13 and age <= 19:
#     print("Teenager")
# elif age >= 20:
#     if age<65:
#         print("Adult")
#     elif age >= 65:
#         print("Senior")
# else:
#     print("Wrong input")

# 
# Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:

# If the customer is a member:
#     If the purchase amount is $50 or more, print "Eligible for 10% discount".
#     Otherwise, print "Eligible for 5% discount".
# If the customer is not a member:
#     If the purchase amount is $100 or more, print "Eligible for 5% discount".
#     Otherwise, print "No discount".
# 
# membersh1p=input("Are you a member? ")
# membership=membersh1p.upper()

# if membership == "YES":
#     purchase_amount= int(input("Enter Bill: "))
#     if purchase_amount >= 50:
#         print("Eligible for 10% Discount")
#     else:
#         print("Eligible for 5% Discount")
# elif membership == "NO":
#     purchase_amount= int(input("Enter Bill: "))
#     if purchase_amount >= 100:
#         print("Eligible for 5% Discount")
#     else:
#         print("No discount")
# else:
#     print("Wrong input")
 
# create the same ATM machine program that we do in last class.

# Features:
# Affiliated Card Requirement:
# Allow transactions only if the user has an affiliated card (affiliated_card is True) and the user's age is less than 60 years (age < 60).

# Senior Citizen Exception:
# Allow transactions for senior citizens (is_senior_citizen is True) regardless of their affiliated card status.

# Government Employee Exception:
# Allow transactions for government employees (is_govt_employee is True) regardless of their age and affiliated card status.

# Additional Charge for Low Grade:
# Charge an additional 10 Rs for transactions if the user's grade (grade) is less than 18.

# # hint: filename: if_statement/if_with_nested_if.py
# bank transaction

# balance=int(input("Enter deposit money: "))
# User_age=int(input("Enter Age: "))
# withdraw_amount= int(input("Enter Withdraw Amount: "))
# affiliated_card= True
# is_senior_citizen= True
# is_govt_employee= True
# High_Grade=True
# Low_Grade=False
# if balance<= withdraw_amount:
#     print("Insufficient balance")

# elif User_age<60 and affiliated_card == True:
#     balance-=withdraw_amount
#     print("Current balance",balance)
# elif User_age>=60 and is_senior_citizen:
#     balance-= withdraw_amount
#     print("Current balance",balance)
# elif is_govt_employee==True:
#     if High_Grade==True:
#         balance-= withdraw_amount
#         print("Current balance",balance)
#     elif Low_Grade==True:
#         balance-= withdraw_amount+10
#         print("Current balance",balance)
# else:
#     print("wrong input")




        