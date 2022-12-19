import re
from itertools import zip_longest

"""
START FUNCTIONS
"""

def FormatCrates(crates):
    # Format crates into a list of rows, converting empty spaces into 'X'
    # The idea is creating a grid replacing the empty spaces for X in order to easily rearrange it
    crates = [re.sub(" {4}", "X", crate) for crate in crates]       # replace 4 paces for X
    crates = [re.sub("\[|\]", "", crate) for crate in crates]       # remove square brackets
    crates = [''.join(crate.split()) for crate in crates]           # remove all spaces
    crates.pop()                                                    # remove the \n
    crates.reverse()                                                # put numbers first
    return crates

def CreateColumns(crate_list):
    # combine the nth char of each string of the list to make columns
    crate_columns = [list(x) for x in zip_longest(*crate_list)]
    # remove the X
    crate_columns = [[x for x in crate if x != 'X'] for crate in crate_columns]
    return crate_columns


def MoveCrates(crates, instructions):
    # crates: list of colums (each column is a list starting with the index and followed by the crates, bottom to top)
    for inst in instructions:
        times = inst[0]
        origin = inst[1]
        dest = inst[2]
        # crate[0][0] is the index, look for origin and destination
        cr_origin = next(crate for crate in crates if crate[0][0] == origin)
        cr_dest = next(crate for crate in crates if crate[0][0] == dest)
        # move the crates
        for i in range(int(times)):
            if not cr_origin[-1].isdigit():         # make sure not moving the index
                cr_dest.append(cr_origin[-1])
                cr_origin.pop()
    return crates

def PrintTopCrate(crates):
    top_crates = [crate[-1] for crate in crates]                # put the top crat of each column in a list
    print(top_crates)

"""
END FUNCTIONS
"""

instructions = []
crates = []

# Separate the crates (+ column index) from the instructions
with open ("input.txt", "r") as input:
    for line in input:
        if line.startswith("move"):
            instructions.append(line)
        else:
            crates.append(line)

print (crates, instructions)

# Format instructions into a list of lists of numbers (remove the words)
instructions = [re.findall(r'\d+', instruction) for instruction in instructions]

crates = FormatCrates(crates)

crates = CreateColumns(crates)

crates = MoveCrates(crates, instructions)

PrintTopCrate(crates)
