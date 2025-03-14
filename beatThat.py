import random

def rollDice():
    return random.randint(1, 6)

def playerturns(playername):
    roll1 = rollDice()
    roll2 = rollDice()
    if roll1 > roll2:
        turnscore = str(roll1) + str(roll2)
    else:
        turnscore = str(roll2) + str(roll1)
    print(f"{playername} result this round: {turnscore}")
    return int(turnscore), turnscore

def beatThat():
    player1name = input("Enter player 1 name: ")
    player2name = input("Enter player 2 name: ")
    player1score = 0
    player2score = 0
    player1turn = True
    player1turnscore_str = "00"
    player2turnscore_str = "00"

    print(f"{player1name}'s turn.")
    player1turnscore, player1turnscore_str = playerturns(player1name)
    player1score += player1turnscore
    print(f"{player1name} current points: {player1score}")
    print("*" * 50)

    print(f"{player2name}'s turn.")
    player2_turnscore, player2turnscore_str = playerturns(player2name)
    player2score += player2_turnscore
    print(f"{player2name} current points: {player2score}")
    print("*" * 50)

    while player1score < 100 and player2score < 100:
        if player1turn:
            print(f"{player1name}'s turn.")
            player1turnscore, player1turnscore_str = playerturns(player1name)
            player1score += player1turnscore
            print(f"{player1name} current points: {player1score}")
            print("*" * 50)
        else:
            print(f"{player2name}'s turn.")
            player2_turnscore, player2turnscore_str = playerturns(player2name)
            player2score += player2_turnscore
            print(f"{player2name} current points: {player2score}")
            print("*" * 50)

        if player1turnscore_str > player2turnscore_str:
            player1turn = True
        else:
            player1turn = False

        print("_" * 50)

    if player1score >= 100:
        print(f"{player1name} wins!")
    else:
        print(f"{player2name} wins!")

beatThat()