file = open('day2-challenge1.input')
print file.name
total_paper = 0

for line in file:
    sides = [x.strip('\n') for x in line.split('x')]
    print sides
    side_1 = int(sides[0]) * int(sides[1])
    side_2 = int(sides[1]) * int(sides[2])
    side_3 = int(sides[0]) * int(sides[2])
    extra = min([side_1, side_2, side_3])
    total_paper += 2*side_1 + 2*side_2 + 2*side_3 + extra
    
print total_paper    