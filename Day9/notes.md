## Requisites
- Head and tail start in the bottom-left corner of the grid
- Head moves a given amount of steps. We need to register every step of the tail following it.
- We must count all the positions the **tail** has visited at least once
- The starting position counts as a visited position

## Tail Movement

- The tail *won't move* if it is touching the head (diagonals count)
- If the head is ever two steps **directly** up, down, left or right
  - The tail will move one step in that direction
- If the head and tail aren't touching and aren't in the same row or column
  - The tail always moves one step **diagonally**
  - *Apparently, the tail moves to the space previously occupied by the head*

## What do we need to check for?

- Are head & tail touching?
- If they're not touching, are they in the same row/column?
- What positions have been visited by tail? (maybe use set?)
  - Keep a list of tuples (x, y)
  - If we move R/L -> Add/Subtract to x
  - If we move U/D -> Add/Subtract to y

## Process movement
- Head movement ✅
  - Follow the instruction as a whole step ✅
- Tail movement
  - Check head position
    - It is in the same row/column
      - Move towards head
    - It is *not* in the same row/column
      - Move diagonally
        - +(1, 1):   North-East
        - +(-1, 1):  North-West
        - +(1, -1):  South-East
        - +(-1, -1): South-East
      - Move towards head
    - Register every visited position
