
import random


row1 = ["", "|", "", "|", ""]
row2 = ["", "|", "", "|", ""]
row3 = ["", "|", "", "|", ""]


def board(row1, row2, row3):
    print(f"""
    {row1}
    -----------------------
    {row2}
    -----------------------
    {row3}
    """)


def game(board, row1, row2, row3, play, p, pplays):
    if play in plays:
        print("THAT SPOT HAS ALREADDY BEEN TAKEN!")
    if p == 1:
        coin = "x"
        if play == "a1":
            row1.insert(0, coin)
            row1.pop(1)
            plays.append("a1")

            pplays.pop(1)
        if play == "a2":
            row1.insert(2, coin)
            row1.pop(3)
            plays.append("a2")

        if play == "a3":
            row1.insert(4, coin)
            row1.pop(5)
            plays.append("a3")

        if play == "b1":
            row2.insert(0, coin)
            row2.pop(1)
            plays.append("b1")

        if play == "b2":
            row2.insert(2, coin)
            row2.pop(3)
            plays.append("b2")

        if play == "b3":
            row2.insert(4, coin)
            row2.pop(5)
            plays.append("b3")

        if play == "c1":
            row3.insert(0, coin)
            row3.pop(1)
            plays.append("c1")

        if play == "c2":
            row3.insert(2, coin)
            row3.pop(3)
            plays.append("c2")

        if play == "c3":
            row3.insert(4, coin)
            row3.pop(5)
            plays.append("c3")
    else:
        coin = "o"
        if play == "a1":
            row1.insert(0, coin)
            row1.pop(1)
            plays.append("a1")
            board(row1, row2, row3)
            pplays.pop(1)
        if play == "a2":
            row1.insert(2, coin)
            row1.pop(3)
            plays.append("a2")
            board(row1, row2, row3)
        if play == "a3":
            row1.insert(4, coin)
            row1.pop(5)
            plays.append("a3")
            board(row1, row2, row3)
        if play == "b1":
            row2.insert(0, coin)
            row2.pop(1)
            plays.append("b1")
            board(row1, row2, row3)
        if play == "b2":
            row2.insert(2, coin)
            row2.pop(3)
            plays.append("b2")
            board(row1, row2, row3)
        if play == "b3":
            row2.insert(4, coin)
            row2.pop(5)
            plays.append("b3")
            board(row1, row2, row3)
        if play == "c1":
            row3.insert(0, coin)
            row3.pop(1)
            plays.append("c1")
            board(row1, row2, row3)
        if play == "c2":
            row3.insert(2, coin)
            row3.pop(3)
            plays.append("c2")
            board(row1, row2, row3)
        if play == "c3":
            row3.insert(4, coin)
            row3.pop(5)
            plays.append("c3")
            board(row1, row2, row3)
    winner(row1, row2, row3)


def winner(row1, row2, row3):
    if row1[0] and row1[2] and row1[4] == "x":
        board(row1, row2, row3)
        print("You Win!")
        quit()
    if row2[0] and row2[2] and row2[4] == "x":
        board(row1, row2, row3)
        print("You Win!")
        quit()
    if row3[0] and row2[2] and row3[4] == "x":
        board(row1, row2, row3)
        print("You Win!")
        quit()
    if row1[0] and row2[0] and row3[0] == "x":
        board(row1, row2, row3)
        print("You Win!")
        quit()
    if row1[2] and row2[2] and row3[2] == "x":
        board(row1, row2, row3)
        print("You Win!")
        quit()
    if row1[4] and row2[4] and row3[4] == "x":
        board(row1, row2, row3)
        print("You Win!")
        quit()
    if row1[0] and row2[2] and row3[4] == "x":
        board(row1, row2, row3)
        print("You Win!")
        quit()
    if row1[4] and row2[2] and row3[0] == "x":
        board(row1, row2, row3)
        print("You Win!")
        quit()
    if row1[0] and row1[2] and row1[4] == "o":
        board(row1, row2, row3)
        print("You Win!")
        quit()
    if row2[0] and row2[2] and row2[4] == "o":
        board(row1, row2, row3)
        print("Computer Win!")
        quit()
    if row3[0] and row2[2] and row3[4] == "o":
        board(row1, row2, row3)
        print("Computer Win!")
        quit()
    if row1[0] and row2[0] and row3[0] == "o":
        board(row1, row2, row3)
        print("Computer Win!")
        quit()
    if row1[2] and row2[2] and row3[2] == "o":
        board(row1, row2, row3)
        print("Computer Win!")
        quit()
    if row1[4] and row2[4] and row3[4] == "o":
        board(row1, row2, row3)
        print("Computer Win!")
        quit()
    if row1[0] and row2[2] and row3[4] == "o":
        board(row1, row2, row3)
        print("Computer Win!")
        quit()
    if row1[4] and row2[2] and row3[0] == "o":
        board(row1, row2, row3)
        print("Computer Win!")
        quit()


plays = []
pplays = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]


print("Welcome to tic tac toe")
board(row1, row2, row3)
played = 0
while played <= 9:
    play = input("What is your move: ")
    if play == "q":
        break
    game(board, row1, row2, row3, play, 1, pplays)
    cp = random.choice(pplays)
    while cp in plays:
        cp = random.choice(pplays)
    game(board, row1, row2, row3, cp, 2, pplays)
    played += 2
    if played == 10:
        print("Game Over! Tie!")
        break
