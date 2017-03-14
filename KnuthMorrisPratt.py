import sys

arguments = sys.argv

input = arguments[1]
#search_string = arguments[2]

#print(input)
#print(search_string)

genome = ""
with open(input) as inputfile:
    i = 0
    for line in inputfile:
        if i != 0:
            genome+=line.strip()
        i += 1

