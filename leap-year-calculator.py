print("created by hussainatphysics@gmail.com(hussainsha syed")
print("welcome to leap year calculator")

"""
we are creating leap year calculator....i am adding but variable as i am creating exe file noting morethan this

"""


year = int(input("Which year do you want to check? "))
but1=input("press enter")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("it is a leap year")
        else:
            print("it is not a leap year")

    else:
        print("it is a leap year")

else:
    print("It is not a leap year")
print()

but2= input("press enter for BYE!!!!!!!!!!!!!!!dear")