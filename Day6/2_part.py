#Day 6 Part 2

# Check if there are repeated chars in the given chunk
# If no repeated chars, return False to stop the loop in main
def CheckChunk(chunk):
    char_count = {}
    for char in chunk:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for char, count in char_count.items():
        if count > 1:
            return True
    return False

"""
End of Functions
"""


with open ("input.txt", 'r') as input:
    datastream = input.read()

# Same process than in part 1, just change the offset (+10) and the slice.
count = 13
condition = True
while condition:
    chunk = datastream[:14]
    condition = CheckChunk(chunk)
    count += 1
    datastream = datastream[1:]
print(count)
