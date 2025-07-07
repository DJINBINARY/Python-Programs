# Rock paper season program in python by DJ
import  random
options  = ["rock","paper","seasor"]
print("Welcome to the Rock Paper Seasor Game \n ")
print("Devloped by Divyanshu Joshi \n ")
print("--------------------------------------")
name = input("Enter your name :")


user_choice = input("Enter your move : rock,paper,seasor : ")
comp_choice =  random.choice(options)
print(f"User choice = {user_choice} \n Computer choice = {comp_choice}")

if(user_choice == comp_choice):
    print("Both chooses same match tie ")

elif(user_choice == "rock" and comp_choice == "paper"):
    print("computer win !!")

elif(user_choice == "rock" and comp_choice=="seasor"):
    print(f"{name} Win !!!")

elif(user_choice == "paper" and comp_choice == "rock"):
    print(f"{name} win ")

elif(user_choice == "paper" and comp_choice == "seasor"):
    print("computer win ")

elif(user_choice == "seasor" and comp_choice == "rock"):
    print("computer win ")

elif(user_choice == "seasor" and comp_choice == "paper"):
    print(f"{user} win ")

else:
    print("wrong input ")
