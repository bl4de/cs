#!/usr/bin/python

f = open("p022_names.txt")
# f = open("022_temp_names.txt")
names = f.readlines()[0].split(",")
names.sort()

wage = 0
name_score = 0
total_score = 0

for name in names:
    letters = list(name)
    name_wage = 0
    name_score += 1

    for letter in letters:
        if letter != '"':
            letter_wage = ord(letter) - 64
            name_wage += letter_wage        # name wage calculated

    total_score += name_wage * name_score

    if name == '"COLIN"':
        print "COLIN: ", name_wage, " ", name_score

print total_score


