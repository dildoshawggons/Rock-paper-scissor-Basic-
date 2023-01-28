player_wins = 0
computer_wins = 0
Name = input("What's your name")
while computer_wins < 2 and player_wins < 2:
         print(f"{Name} won :{player_wins}  Computer won:{computer_wins}")
         import random
         from random import randint
         H = "Joining game"
         #Choices----------------------------------
         print("Rock..")
         print("paper..")
         print("scissors..")
         #Player 1 Input value ---------------------------
         player_1= input(f"Make your move {Name}\n")
         #Player 1 Input value----------------------
         print("No cheating\n\n" * 100)
         #Computer------------------------------
         Random_Numbers = random.randint(0,2)
         if Random_Numbers == 0:
            computer = "paper"
         elif Random_Numbers == 1:
            computer = "rock"
         elif Random_Numbers == 2:
            computer = "scisoors"
            print(f"Computer plays {computer}")
         # Player 1------------------------------------------
         if player_1 == "Rock" and computer == "scissors":
            print(f"{Name} WINS")
            player_wins += 1
         elif player_1 == "paper" and computer == "rock":
            print(f"{Name} WINS")
            player_wins += 1
         elif player_1 == "scissors" and computer == "paper":
            print(f"{Name} WINS")
            player_wins += 1
         elif player_1 == computer:
            print("Tie go again")
         #----------------------------------------------------
         elif computer == "Rock" and player_1 == "scissors":
            print("Computer wins")
            computer_wins += 1
         elif computer == "paper" and player_1 == "rock":
            print("Computer wins")
            computer_wins += 1
         elif computer == "scissors" and player_1 == "paper":
            print("Computer wins")
            computer_wins += 1
         elif computer == player_1:
             print("Tie go again")
         #-----------------------------------------------------
print(f"Final score[]: {Name} won :{player_wins}  Computer won:{computer_wins}")
     computer = "paper"
     elif Random_Numbers == 1:
        computer = "rock"
     elif Random_Numbers == 2:
        computer = "scissors"
        print(f"Computer plays {computer}")
     # Player 1------------------------------------------
     if player_1 == "Rock" and computer == "scissors":
        print(f"{Name} WINS")
        player_wins += 1
     elif player_1 == "paper" and computer == "rock":
        print(f"{Name} WINS")
        player_wins += 1
     elif player_1 == "scissors" and computer == "paper":
        print(f"{Name} WINS")
        player_wins += 1
     elif player_1 == computer:
        print("Tie go again")
     #----------------------------------------------------
     elif computer == "Rock" and player_1 == "scissors":
        print("Computer wins")
        computer_wins += 1
     elif computer == "paper" and player_1 == "rock":
        print("Computer wins")
        computer_wins += 1
     elif computer == "scissors" and player_1 == "paper":
        print("Computer wins")
        computer_wins += 1
     elif computer == player_1:
         print("Tie go again")
     #-----------------------------------------------------
print(f"Final score[]: {Name} won :{player_wins}  Computer won:{computer_wins}")
