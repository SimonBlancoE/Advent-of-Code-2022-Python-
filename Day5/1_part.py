"""
Process text:
    Create separate files for instructions and crates

Read top crate
Move top crate (origin, dest, times)
"""

import re
from itertools import zip_longest


def MoveTopCrate (times, origin, dest):
    pass

def FormatCrates(crates):
    # Format crates into a list of lists of columns, converting empty spaces into 'X'
    crates = [re.sub(" {4}", empty_space, crate) for crate in crates] 
    crates = [re.sub("\[|\]", "", crate) for crate in crates]
    crates = [re.sub("X", "", crate) for crate in crates]
    crates = [''.join(crate.split()) for crate in crates]
    crates.pop()
    crates.reverse()
    return crates

def CreateColumns(crate_list):
#    print(crate_list)
    crate_columns = [list(x) for x in zip_longest(*crate_list)]
#    print(crate_columns)
    return crate_columns


def MoveCrates(crates, instructions):
    for inst in instructions:
        times = inst[0]
        origin = inst[1]
        dest = inst[2]
        buffer = None
        #print(origin)
        # do the following with list comp -> buffer = [.....
        for crate in crates:
            if crate[0] == origin:
                print(crate)
                while buffer == None:
                    buffer = crate[-1]
                    crate.pop()
                print(crate)



instructions = []
crates = []
instr_numeric = []
empty_space = "X"

with open ("sampleinput.txt", "r") as input:
    for line in input:
        if line.startswith("move"):
            instructions.append(line)
        else:
            crates.append(line)

#print (crates, instructions)

# Format instructions into a list of lists of numbers
#new_instructions = [[char for instruction in instructions] for char in instruction if char.isdigit()] ==> ['1', '2', '1', '3', '1', '3', '2', '2', '1', '1', '1', '2']

instructions = [[char for char in instruction if char.isdigit()] for instruction in instructions]
print(instructions)

crates = FormatCrates(crates)
#print(crates)

crates = CreateColumns(crates)
print(crates)

MoveCrates(crates, instructions)

