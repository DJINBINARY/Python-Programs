#program to give grades to the students
marks = int(input("Enter your final marks(between 1 to 100 : "))

if(marks>90 and  marks<=100):
    print("Wow... you got the A+ grade")

elif(marks>80 and  marks<=90):
    print("You got the A grade")

elif(marks>70 and marks<=80):
    print("You got the B+ grade")

elif(marks>60 and marks<=70):
    print("You got the B grade")

elif(marks>50 and marks<=60):
    print("You got the C+ grade")

elif(marks>40 and marks<=50):
    print("you got the C grade")

elif(marks>0 and marks<=40):
    print("You are fail !!! better luck next time ")

else:
    print("Please enter a valid marks between 0 to 100")

