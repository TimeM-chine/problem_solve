
import turtle
string = 'DDDDRRURRRRRRDRRRRDDDLDDRDDDDDDDDDDDDRDDRRRURRUURRDDDDRDRRRRRRDRRURRDDDRRRRUURUUUUUUULULLUUUURRRRUULLLUUUULLUUULUURRURRURURRRDDRRRRRDDRRDDLLLDDRRDDRDDLDDDLLDDLLLDLDDDLDDRRRRRRRRRDDDDDDRR'
my_string = 'DDDDRRURRRRRRRDRRRDDDLDDRDDDDDDDDDDDDRDRDRRURRUURRDDDDRDRRRRRRDRRURRDDDRRRRUURUUUUUUUULLLUUUURRRRUULLLUUUULLUUULUURRURRURURRRDRDRRRRDRDRDDLLLDDRRDDRDDLDDDLLDDLLLDLDDDLDDRRRRRRRRRDDDDDDRR'
print(len(string))
p = turtle.Pen()
s = turtle.Screen()
s.setworldcoordinates(0,0,320,520)

def str2list(string):
    routine = [(1, 1)]
    for i in string:
        if i == 'D':
            temp = (routine[-1][0] + 1, routine[-1][1])
            routine.append(temp)
        if i == 'U':
            temp = (routine[-1][0] - 1, routine[-1][1])
            routine.append(temp)
        if i == 'L':
            temp = (routine[-1][0], routine[-1][1] - 1)
            routine.append(temp)
        if i == 'R':
            temp = (routine[-1][0], routine[-1][1] + 1)
            routine.append(temp)
    return routine

def list2str(li):
    direction = ''
    length = len(li)
    for i in range(length - 1, 0, -1):
        # print(i)
        li[i] = (li[i][0] - li[i - 1][0], li[i][1] - li[i - 1][1])
    li.pop(0)
    for i in li:
        # print(i)
        if i == (1, 0):
            direction += 'D'
        if i == (0, 1):
            direction += 'R'
        if i == (-1, 0):
            direction += 'U'
        if i == (0, -1):
            direction += 'L'
    print(direction)

def paint(list):
    for i in list:
        p.goto(i[0]*10,i[1]*10)

routine = str2list(string)
my_routine = str2list(my_string)
#
# print(routine)
print(my_routine)
def home():
    p.penup()
    p.goto(1,1)
    p.pendown()

home()
paint(routine)
p.color('red')
home()
paint(my_routine)

turtle.done()
