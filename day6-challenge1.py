import re

grid_of_lights = []
for i in range(1000):
    new = []
    for j in range(1000):
        new.append(False)
    grid_of_lights.append(new)

def turn_on(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid_of_lights[x][y] = True

def turn_off(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid_of_lights[x][y] = False            

def toggle(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid_of_lights[x][y] = not grid_of_lights[x][y]
            
def printer():
    print "Grid: "
    for light in grid_of_lights:
        print light
    print "\n"    
    
def counter():
    count = 0
    for line in grid_of_lights:
        for light in line:
            if light:
                count += 1
    print count
    
def parser(line):
    x = []
    y = []
    coords = re.findall(r"\d*,\d*", line)
    for coord in coords:
        x.append(int(coord.split(',')[0]))
        y.append(int(coord.split(',')[1]))
    # now check what action we're performing
    tog = 'toggle'
    on = 'turn on'
    off = 'turn off'
    if tog in line:
        toggle(x[0], x[1], y[0], y[1])
    elif on in line:
        turn_on(x[0], x[1], y[0], y[1])
    elif off in line:
        turn_off(x[0], x[1], y[0], y[1])
    else:
        print 'whoops'
    

parser('turn on 0,0 through 999,999')
counter()
