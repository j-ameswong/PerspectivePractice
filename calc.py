from random import randint
import math

def give_angles(min_angle, n_angles):
    angles = []
    for x in range(n_angles):
        if x!=(n_angles-1):
            try:
                a = randint(min_angle, 360 - sum(angles) - (min_angle*(n_angles-x-1)))
                angles.append(a)
            except:
                raise Exception('That\'s not possible!')

        else:
            angles.append(360-sum(angles))

    return(angles)

def get_lengths(n_lines, min_l, max_l):
    lines = []
    for x in range(n_lines):
        lines.append(randint(min_l, max_l))
    
    return(lines)

''' I feel like there's a mathematical way to solve this that's so 
    much simpler but I have no bloody idea so I'm just gonna do this '''
def get_end_coords(start_x, start_y, length, angle):
    add_x = 0
    add_y = 0
    quadrant = 0
    while angle-90>0:
        quadrant += 1
        angle -= 90

    if quadrant == 0:
        add_x = length * math.sin(math.radians(angle))
        add_y = length * -(math.cos(math.radians(angle)))
    
    elif quadrant == 1:
        add_x = length * math.cos(math.radians(angle))
        add_y = length * math.sin(math.radians(angle))
    
    elif quadrant == 2:
        add_x = length * -math.cos(90-math.radians(angle))
        add_y = length * math.sin(90-math.radians(angle))

    elif quadrant == 3:
        add_x = length * -math.cos(math.radians(angle))
        add_y = length * -math.sin(math.radians(angle))

    return(start_x + add_x, start_y + add_y)


    


# print(f'Sum is {sum(give_angles2(30,5))}', give_angles2(10,5))
        

