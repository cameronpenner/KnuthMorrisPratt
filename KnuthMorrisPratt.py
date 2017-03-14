import sys

#get user input from arguments
arguments = sys.argv

input = arguments[1]
search_string = arguments[2]

print("opening file: " + input)
print("searching for string: " + search_string)

#load in genome from file
genome = ""
with open(input) as inputfile:
    i = 0
    for line in inputfile:
        if i != 0:
            genome+=line.strip()
        i += 1

#build shift table
shift_table = [0] * (len(search_string) + 1)

i = 0
j = shift_table[0] = -1

while i < len(search_string):
    while j > -1 and search_string[i] != search_string[j]:
        j = shift_table[j]
    i += 1
    j += 1

    if i < len(search_string) and search_string[i] == search_string[j]:
        shift_table[i] = shift_table[j]
    else:
        shift_table[i] = j

print("Shift table: "+str(shift_table))

#search using KMP
def search(input, pattern):
    j = 0
    i = 0
    occurrences = 0

    return occurrences

#invert a string
def reverse(to_reverse):
    reversed = to_reverse[::-1]
    i = 0
    compliment = ''
    for char in reversed:
        if char == 'G':
            compliment += 'C'
        elif char == 'C':
            compliment += 'G'
        elif char == 'T':
            compliment += 'A'
        elif char == 'A':
            compliment += 'T'
        i += 1
    return compliment

occurs = search(genome, search_string)
print("Occurrences of " + search_string + ": " + str(occurs))

occurs = search(genome, reverse(search_string))
print("Occurrences of reverse compliment " + str(reverse(search_string)) + ": " + str(occurs))