file = open('day2-challenge1.input')
total_ribbon = 0

for line in file:
    sides = [int(x.strip('\n')) for x in line.split('x')]
    face_1 = [sides[0], sides[1]]
    face_2 = [sides[1], sides[2]]
    face_3 = [sides[0], sides[2]]
    per = min([2 * (face_1[0] + face_1[1]),2 * (face_2[0] + face_2[1]),2 * (face_3[0] + face_3[1])])
    vol = reduce(lambda x, y: x * y, sides)
    total_ribbon += per + vol
    
print total_ribbon   