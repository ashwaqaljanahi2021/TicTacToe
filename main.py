import art
import random
print(art.logo)
BOARD = list("  |      | \n------------ \n  |      | \n------------ \n  |      |  ")

positions = {
    1: 1,
    2: 5,
    3: 10,
    4: 26,
    5: 31,
    6: 36,
    7: 52,
    8: 57,
    9: 62
}

positions_used = {}
num = 0


def print_board():
    print("Welcome to Tic Tac Toe\n")
    print("".join(BOARD))


print_board()
flag = False
mode = input("One player or Two? y or n")
if mode == 'y':
    flag = True

input1 = input("Would you like to be X or O?\n").upper()
if input1 == 'O':
    input2 = 'X'
else:
    input2 = 'O'


def print_board():
    print("Welcome to Tic Tac Toe\n")
    print("".join(BOARD))


def update_board(x, player):
    global BOARD
    for i in range(len(BOARD)):
        if positions[x]:
            BOARD[positions[x]] = player


def position(player):
    global positions_used, num
    num += 1
    x = int(input(f"what position would you like? (1-9) Player {num}\n"))
    while x in positions_used:
        x = int(input(f"OOPS this position is already filled! what position would you like? Player 1\n"))
    positions_used[x] = player
    update_board(x, player)
    if num == 2:
        num = 0
    print("".join(BOARD))

def position_bot(player):
    global positions, positions_used, num
    num += 1
    if num == 1:
        x = int(input(f"what position would you like? (1-9) Player 1\n"))
        while x in positions_used:
            x = int(input(f"OOPS this position is already filled! what position would you like? Player 1\n"))
        positions_used[x] = player
        update_board(x, player)
    if num == 2:
        num = 0
    if num == 0:
        rand = random.choice(list(positions.keys()))
        while rand in positions_used:
            rand = random.choice(list(positions.keys()))
        positions_used[rand] = player
        update_board(rand, player)
        print("".join(BOARD))


def check_score():
    if 1 in positions_used and 2 in positions_used and 3 in positions_used and positions_used[1] == positions_used[
        2] and positions_used[3] == positions_used[1]:
        print("GAME OVER")
        return False
    if 4 in positions_used and 5 in positions_used and 6 in positions_used and positions_used[4] == positions_used[
        6] and positions_used[4] == positions_used[5]:
        print("GAME OVER")
        return False
    if 7 in positions_used and 8 in positions_used and 9 in positions_used and positions_used[7] == positions_used[
        8] and positions_used[8] == positions_used[9]:
        print("GAME OVER")
        return False
    if 1 in positions_used and 4 in positions_used and 7 in positions_used and positions_used[1] == positions_used[
        4] and positions_used[4] == positions_used[7]:
        print("GAME OVER")
        return False
    if 2 in positions_used and 5 in positions_used and 8 in positions_used and positions_used[2] == positions_used[
        5] and positions_used[5] == positions_used[8]:
        print("GAME OVER")
        return False
    if 3 in positions_used and 6 in positions_used and 9 in positions_used and positions_used[3] == positions_used[
        6] and positions_used[6] == positions_used[9]:
        print("GAME OVER")
        return False
    if 1 in positions_used and 5 in positions_used and 9 in positions_used and positions_used[1] == positions_used[
        5] and positions_used[5] == positions_used[9]:
        print("GAME OVER")
        return False
    if 3 in positions_used and 5 in positions_used and 7 in positions_used and positions_used[3] == positions_used[
        5] and positions_used[7] == positions_used[5]:
        print("GAME OVER")
        return False
    if len(positions_used) == 9:
        print("TIED")
        return False
    return True


if (flag):
    while check_score():
        position_bot(input1)
        if not check_score():
            print("".join(BOARD))
            break
        position_bot(input2)


else:
    while check_score():
        position(input1)

        if not check_score():
            print("".join(BOARD))
            break
        position(input2)
