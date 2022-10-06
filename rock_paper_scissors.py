import random

name = input("hey dude. enter your name:").upper()
print("HELLO",name," ,WELCOME TO ROCK_PAPER_SCISSOR GAME")
user_wins = 0
computer_wins = 0
tied = 0
options = ["rock","paper","scissor"]
while True:
    user_input = input("type rock/paper/scissor or Q to quit a game  :").lower()
    if user_input == "q":
        break
    elif user_input not  in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked",computer_pick,".")
    if user_input == "rock" and computer_pick == "scissor":
        print("hey!! you won")
        user_wins+=1
    elif user_input == "paper" and computer_pick == "rock":
        print("hey!! you won")
        user_wins+=1
    elif user_input == "scissor" and computer_pick == "paper":
        print("hey!! you won")
        user_wins+=1
    elif user_input == "scissor" and computer_pick == "scissor":
        print("Tied...")
        tied += 1
    elif user_input == "paper" and computer_pick == "paper":
        print("tied...")
        tied += 1
    elif user_input == "rock" and computer_pick == "rock":
        print("tied...")
        tied += 1
    else:
        print("you lost!")
        computer_wins += 1
print(name,",you won",user_wins,"times.")
print("computer won",computer_wins,"times.")
print(tied," times was tied")
print("goodbye!! ",name)

