"""
 PART 2: Find the common letter in three-by-three lines

- Take three lines
- Search for repeating letter in all lines       -> RepItem
- Convert letter to priority number               -> PriNum
- Sum priority

"""


def RepItem(ruck):
    for a in ruck[0]:
        for b in ruck[1]:
            if b == a:
                for c in ruck[2]:
                    if c == b:
                        return c

def PriNum(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    priority = 1
    if letter.isupper():
        priority += 26
    for item in alphabet:
        if item == letter.lower():
            return priority
        else:
            priority += 1



with open ("input.txt", "r") as input:
    pri_sum = 0
    pack_3_ruck = []
    for line in input:
        pack_3_ruck.append(line.strip())
        if len(pack_3_ruck) == 3:
            print(pack_3_ruck)
            letter = RepItem(pack_3_ruck)
            print (letter)
            pri = PriNum(letter)
            pri_sum += pri
            print(pri_sum)
            pack_3_ruck.clear()
