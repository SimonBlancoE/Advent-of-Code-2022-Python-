
"""
Process the file:
    split by delimiter (,)
    split by delimiter (-)
    return list with 4 numbers

Compare numbers in list:
    [0][0]
    [0][1]
    [1][0]
    [1][1]
    (2nd item contained in 1st)
    pos[3] must be higher than pos[1]
    pos[2] must be higher than pos[4]
    (1st item contained in 2nd)
    pos[1] must be higher than pos[3]
    pos[4] must be higher than pos[2]

"""

def ProcessSection(section):
    ret_list = []
    pair = section.split(',')
    for item in pair:
        ret_list.append(item.split('-'))
    return ret_list

def IsContained (IDGroup):
    if int(IDGroup[1][0]) >= int(IDGroup[0][0]) and int(IDGroup[0][1]) >= int(IDGroup[1][1]):
        return 1
    elif int(IDGroup[0][0]) >= int(IDGroup[1][0]) and int(IDGroup[1][1]) >= int(IDGroup[0][1]):
        return 1
    else:
        return 0


with open ("input.txt", "r") as input:
    result = 0
    for line in input:
        result += IsContained(ProcessSection(line.strip()))
    print(result)
