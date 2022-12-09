"""  POINTS
Rock = 1 Points       (AX)
Paper = 2 Points      (BY)
Scissors = 3 Points   (CZ)

Win = 6 Points
Draw = 3 Points
Lose = 0 Points
"""

"""
Store 1st letter in var 1
Store 2nd letter in var 2
Decide winner (or draw)
    A beats Z, draws X
    B beats X, draws Y
    C beats Y, draws Z
Calculate points
"""


def Numberify(hand):                                #Give default points for hand
    if hand == 'A' or hand == 'X':
        return 1
    elif hand == 'B' or hand == 'Y':
        return 2
    elif hand == 'C' or hand == 'Z':
        return 3


def WinLoseDraw(player_hand, opponent_hand):        #Add points for match result
    if player_hand == opponent_hand:
        return 3                                    # It's a draw, get 3 points
    elif player_hand == 1 and opponent_hand == 3:   # Only different case of winning
        return 6
    elif opponent_hand == player_hand - 1:
        return 6
    else:
        return 0


score = 0
with open('input.txt', 'r') as input:
    lines = input.readlines()
    for line in lines:
        p1 = Numberify(line[2])
        op = Numberify(line[0])
        p1 += WinLoseDraw(p1, op)
        score += p1
        p1 = 0
print(score)
