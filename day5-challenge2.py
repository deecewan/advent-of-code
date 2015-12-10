import re
input = open('day5.input')

repeating_pair = re.compile(r"(..).*\1")
split_repeater = re.compile(r"(.).\1")

string = 'uurcxstgmygtbstg'

print repeating_pair.findall(string)
print split_repeater.findall(string)

count_nice = 0

for line in input:
    if len(repeating_pair.findall(line)) and len(split_repeater.findall(line)):
        count_nice += 1
        print line, " was a nice string"
        
print count_nice        