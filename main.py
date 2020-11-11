import random
moves = ["rock","paper","scissors"]
keep_play = "True"
while keep_play == "True":
    computer= random.choice(moves)
    user = input("What is your move: Rock,Paper,Scissors?")
    print("The computer choose",computer)
    if computer == user:
        print("Tie")
    elif user == "rock" and computer == "scissors":
        print("Player Wins!!")
    elif user == "paper" and computer == "scissors":
        print("Computer Wins!!")
    elif user == "rock" and computer == "paper":
        print("Computer Wins!!")
    elif user == "paper" and computer == "rock":
        print("Player Wins!!")
    elif user == "scissors" and computer == "rock":
        print("Computer Wins!!")
    elif user == "scissors" and computer == "paper":
        print("Player Wins!!")

