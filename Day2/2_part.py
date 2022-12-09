"""  POINTS
Rock = 1 Points       (AX)
Paper = 2 Points      (BY)
Scissors = 3 Points   (CZ)

Z - Win = 6 Points
Y - Draw = 3 Points
X - Lose = 0 Points
"""

"""     PSEUDO CODE
Store 1st letter in var 1
Store 2nd letter in var 2
Decide winner (or draw)
    A beats Z, draws X
    B beats X, draws Y
    C beats Y, draws Z
Calculate points
"""


def Numberify(hand):
    if hand == 'A' or hand == 'X':
        return 1
    elif hand == 'B' or hand == 'Y':
        return 2
    elif hand == 'C' or hand == 'Z':
        return 3


def WinLoseDraw(player_hand, opponent_hand):
    if player_hand == opponent_hand:
        return 3       # It's a draw, get 3 points
    elif player_hand == 1 and opponent_hand == 3:
        return 6
    elif opponent_hand == player_hand - 1:
        return 6
    else:
        return 0

def ChooseMyHand(opponent_hand, condition):
    if condition == 'Y':     # I need to draw
        return opponent_hand
    elif condition == 'X':     # I need to lose
        if opponent_hand == 'A':
            return 'Z'
        elif opponent_hand == 'B':
            return 'X'
        else:
            return 'Y'
    else:                       # I need to win 
        if opponent_hand == 'A':
            return 'Y'
        elif opponent_hand == 'B':
            return 'Z'
        else:
            return 'X'

with open('input.txt', 'r') as input:
    lines = input.readlines()
    score = 0
    for line in lines:
        print(line[0], line[2])
        op_hand = line[0]
        cond = line[2]
        p1_hand = ChooseMyHand(op_hand, cond)
        print("p1_hand: " , p1_hand)
        p1 = Numberify(p1_hand)
        print("p1: " , p1)
        op = Numberify(op_hand)
        p1 += WinLoseDraw(p1, op)
        score += p1
        print("score post: " , score)
        p1 = 0

print(score)
