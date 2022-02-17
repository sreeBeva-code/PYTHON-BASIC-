import random

while True:
    choice = ["rock", "paper", "scissors"]
    computer = random.choice(choice)

    player = input("choce your choice:")
    if player not in choice:
      player = None
    while player not in choice:
        player = input("chose your choice in rock ,paper, scissors:")
    if player == computer:
       print("tie")
       print("computer:", computer)
       print("YOU chose :", player)
    elif player == "rock" and computer == "paper":
       print("you win")
       print("computer:", computer)
       print("YOU chose :", player)
    elif player == "paper" and computer == "rock":
      print("you lose")
      print("computer:", computer)
      print("YOU chose :", player)
    elif player == "scissors" and  computer == "paper":
      print("you lose")
      print("computer:", computer)
      print("YOU chose :", player)
    elif player == "paper" and computer == "scissors":
      print("you lose")
      print("computer:", computer)
      print("YOU chose :", player)
    elif player == "rock" and  computer == "scissors":
      print("you win")
      print("computer:", computer)
      print("YOU chose :", player)
    elif player == "scissors" and computer == "rock":
      print("you lose")
      print("computer:", computer)
      print("YOU chose :", player)
    ply=input("you have to confidence play with me ?(yes/no) :")
    if ply!="yes":
     break
print("bye")





