"""
Process text:
    Create separate files for instructions and crates

Read top crate
Move top crate (origin, dest, times)

#Split input in 2 files
with open ("sampleinput.txt", "r") as input:
    for line in input:
        if line.startswith('move'):
            with open ("instructions.txt", "a") as instructions_txt:
                instructions_txt.write(line)
        else:
            with open ("crates.txt", "a") as crates_txt:
                crates_txt.write(line)

def ReadTopCrate():
    print(instr_numeric)
    print (crates[0])
    print (crates, instructions)

"""


import re


def MoveTopCrate (times, origin, dest):
    pass

def CreateCrateMatrix(crates):
#   Return a clean list with only numbers and letters. 
#   Reverse the list so the numbers come first
    new_crates = []
    for crate in crates:
        new_crate = re.sub(" {4}", empty_space, crate)
        remove = "[]"
        for character in remove:
            new_crate = new_crate.replace(character, "")
        new_crates.append(''.join(new_crate.split()))
    new_crates.pop()
    new_crates.reverse()
    print(new_crates)
    return new_crates

def CreateColumns(crate_list):
    print(crate_list)
    l2 = [list(x) for x in zip(*crate_list)]
    print(l2)

instructions = []
crates = []
instr_numeric = []
empty_space = "[X]"

with open ("sampleinput.txt", "r") as input:
    for line in input:
        if line.startswith("move"):
            instructions.append(line)
        else:
            crates.append(line)

print (crates, instructions)

"""
# Lets put all the numbers in the instructions in a list.
for instruction in instructions:
    for char in instruction:
        if char.isdigit():
            instr_numeric.append(char)
"""

#new_instructions = [[char for instruction in instructions] for char in instruction if char.isdigit()] ==> ['1', '2', '1', '3', '1', '3', '2', '2', '1', '1', '1', '2']

new_instructions = [[char for char in instruction if char.isdigit()] for instruction in instructions] 
print(new_instructions)
#crate_matrix=CreateCrateMatrix(crates)
#CreateColumns(crate_matrix)
