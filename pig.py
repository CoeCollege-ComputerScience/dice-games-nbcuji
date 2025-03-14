import random
def rollDice():
    return random.randint(1,6)

def playerturns(playername, turnscore):
  turnscore = 0
  while True:
        roll = rollDice()
        print(f"{playername} rolled a {roll}")
        if roll == 1:
            print(f"Whoops! {playername} rolled a 1. Their turn is over and they scored 0 points.")
            return 0
        else:
            turnscore += roll
            print(f"{playername}'s current points this turn: {turnscore}.")
            choice = input(f"{playername}, would you like to roll and continue? (y/n) ")
            if choice.lower() == "n":
                print(f"{playername} scored {turnscore} points this turn.")
                return turnscore
            else:       
                continue

def pig():
    player1name = input("Enter player 1 name: ")
    player2name = input("Enter player 2 name: ")
    player1score = 0
    player2score = 0
    while player1score < 100 and player2score < 100:
        if input(f"{player1name}, do you want to roll? (y/n) ").lower() == "y":
            print(f"{player1name}'s turn.")
            player1score += playerturns(player1name, player1score)
        print(f"{player1name} current points: {player1score}")
        print("*" * 50)
        
        if input(f"{player2name}, do you want to roll? (y/n) ").lower() == "y":
            print(f"{player2name}'s turn.")
            player2score += playerturns(player2name, player2score)
        print(f"{player2name} current points: {player2score}")
        print("*" * 50)
        
    if player1score >= 100:
        print(f"{player1name} wins!")
        print(f"{player2name} needs to get better at this game...")
    else:
        print(f"{player2name} wins!")
        print(f"{player1name} needs to get better at this game...")

pig() 
    

