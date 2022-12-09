
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
    1st overlap:
        1 <= 3 <= 2
    second overlap:
        3 <= 1 <= 4
"""

def ProcessSection(section):
    ret_list = []
    pair = section.split(',')
    for item in pair:
        ret_list.append(item.split('-'))
    return ret_list

def IsContained (IDGroup):
    if int(IDGroup[0][0]) <= int(IDGroup[1][0]) <= int(IDGroup[0][1]):
        return 1
    elif int(IDGroup[1][0]) <= int(IDGroup[0][0]) <= int(IDGroup[1][1]):
        return 1
    else:
        return 0


with open ("input.txt", "r") as input:
    result = 0
    for line in input:
        result += IsContained(ProcessSection(line.strip()))
    print(result)
