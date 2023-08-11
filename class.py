# Age calculator

age = input("enter your current age ")
age_as_int = int(age)
 
years_remaining = 70 - age_as_int
days_remaining = years_remaining * 365
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52

message = f"you have{days_remaining}days, you have{months_remaining}months,you have{weeks_remaining}weeks"

print(message)



# Leap Year

# year = int(input("enter the year "))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("leap year")
#     else:
#      print("not leepyear")
#   else:
#    print(" leap year")
# else:
#   print("not leap year")



# program to print wheather a person can ride a roller coaster or not.
# there are certain limits if he can ride and diffrent prices
# print("WELCOME TO ROLLER COASTING")
# height= int(input("enter the height"))

 
# if height >= 120:
#     print("you can ride")
# age = int(input("enter the age"))
# if age <=12:
#     print("price is $7")
# elif age <= 18:
#     print ("price is $12")
# photo_graph = input("do you want snap? Y or N" )
# if photo_graph == "Y":
#     print(" price is $34")
    
# else:
#     print("you can not ride")





# print("WELCOME TO ROLLER COASTER RIDE")

# height = int(input("please enter your height"))
# if height >=120:
#     print("you can ride")
# age = int(input("please enter your age"  ))

# if age >= 12:
#     bill = 5
#     print("your ticket token is $5")
# elif age <=18:
#     bill = 10
#     print("your ticket token is $10")
    
# else:
#      age >= 18
#      bill = 15
#      print("ticket token for adults are $15")
    
# want_photo = input("do you want photograph? y or n")
# if want_photo == "y":
#     bill += 3
#     print(f"your total bill amount is {bill}")

# else:
#     print("you gotta grow bit more to ride ")




# def Riding():
#  print("Welcome to the rollercoaster!")
# height = int(input("What is your height? "))

# if height >= 150:
#     print("You can ride!")
#     age = int(input("What's your age? "))

#     if age <= 15:
#         amount = 54
#         print("Riders under 12 have to pay $5.")
#     elif age <= 18:
#         amount = 66
#         print("Riders between 12 and 18 should pay $66.")
#     else:
#         amount = 67
#         print("Riders 18 and older should pay $67.")

#     photo = input("Do you want a photo? Type 'yes' or 'no': ")

#     if photo.lower() == "yes":
#         amount += 9
#         print(f"Your total amount is ${amount}.")
#     else:
#         print("Your total amount is ${amount}.")
# else:
#     print("Sorry, you cannot ride the rollercoaster.")

# Riding()

# print("WELCOME TO ROLLER COASTER RIDE")

# def RollerCoaster():
    
#  height = int(input("please enter your height: "))
#  if height >= 120:
#        print("you  r able to ride")
# age = int(input("please enter your age: "))
# if age >= 12:
#             bill = 5
#             print("your ticket token is $5")
# elif age <= 18:
#             bill = 10
#             print("your ticket token is $10")
# else:
#             bill = 15
#             print("ticket token for adults is $15")

# want_photo = input("do you want a photograph? (y or n): ")
# if want_photo == "y":
#             bill += 3
#             print(f"your total bill amount is {bill}")
# else:
#            print("Enjoy your ride")
# RollerCoaster()