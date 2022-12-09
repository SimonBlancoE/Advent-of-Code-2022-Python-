"""

- Split line in 2 equal parts                     -> SplitLine
- Search for repeating letter in both parts       -> RepItem
- Convert letter to priority number               -> PriNum
- Sum priority

"""

def SplitLine(line):
    split_list = []
    split_list.append(line[:int(len(line)/2)])
    split_list.append(line[int(len(line)/2):])
    return split_list

def RepItem(ruck):
    for a in ruck[0]:
        for b in ruck[1]:
            if b == a:
                return a

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
    for line in input:
        split_ruck = SplitLine(line.strip())
        letter = RepItem(split_ruck)
        pri = PriNum(letter)
        pri_sum += pri
    print(pri_sum)
