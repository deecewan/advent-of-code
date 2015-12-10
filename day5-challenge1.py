# NB. this did not pass all tests.  it came up 2 strings short of the goal.
# I do not know why.

input = open('day5.input')

import re

double_letters = re.compile(r"([a-z])\1")
vowels = re.compile(r"([aeiou])")
bad = re.compile(r"ab|bc|pq|xy")

count = 0
line_no = 1

for line in input:
    if len(vowels.findall(line)) > 2 and double_letters.findall(line) and not bad.findall(line):
        count += 1
        
print count