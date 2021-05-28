
with open('maze.txt') as f:
    maze = f.read()

# maze = '''010000
# 000100
# 001001
# 110000'''
maze = maze.split('\n')

def check(x, y):
    List = []
    if maze[x][y + 1] == "0":
        List.append((x, y + 1))
    if maze[x + 1][y] == "0":
        List.append((x + 1, y))
    if maze[x - 1][y] == "0":
        List.append((x - 1, y))
    if maze[x][y - 1] == "0":
        List.append((x, y - 1))
    return List


def dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def guiyi(l):
    length = len(l)
    for i in range(length-1):
        if dis(l[length-i-1],l[length-i-2]) !=1:
            # print(l[length-i-1],l[length-i-2])
            l.pop(length-i-2)
    return l
    
def list2str(li):
    direction = ''
    length = len(li)
    for i in range(length - 1, 0, -1):
        li[i] = (li[i][0] - li[i - 1][0], li[i][1] - li[i - 1][1])
    li.pop(0)
    for i in li:
        if i == (1, 0):
            direction += 'D'
        if i == (0, 1):
            direction += 'R'
        if i == (-1, 0):
            direction += 'U'
        if i == (0, -1):
            direction += 'L'
    return direction

def str2list(str):
    routine = [(1,1)]
    for i in str:
        if i =='D':
            temp = (routine[-1][0]+1,routine[-1][1])
            routine.append(temp)
        if i =='U':
            temp = (routine[-1][0]-1,routine[-1][1])
            routine.append(temp)
        if i == 'L':
            temp = (routine[-1][0], routine[-1][1]-1)
            routine.append(temp)
        if i == 'R':
            temp = (routine[-1][0], routine[-1][1]+1)
            routine.append(temp)
    return routine


def paint(Li):
    turtle.pendown()
    for i in Li:
        turtle.goto(i[0]*10,i[1]*10)
    turtle.penup()

answer = []
search_L = []
delete_L = []
maze.insert(0, '1' * len(maze[0]))
maze.append('1' * len(maze[0]))
for i in range(len(maze)):
    maze[i] = '1' + maze[i] + '1'
    # print(maze[i])
start = (1, 1)
end = (len(maze) - 2, len(maze[0]) - 2)
# print(maze[len(maze)-2][len(maze[0])-2])

search_L.append(start)
# print(check(1,3))
count = 0
# while count<15:
flag = 1
while flag:
    count+=1
    i = search_L[0]
    # print("now",i) 
    answer.append(i)
    if i not in delete_L:
        delete_L.append(i)
    res = check(i[0], i[1])
    # for k in res:
    #     if k not in delete_L and k not in search_L:
    #         answer.append(i)
    #         break
    for j in res:
        if j == end:
            answer.append(j)
            # paint(guiyi(answer))
            flag = 0
            break
        if j not in delete_L and j not in search_L:
            search_L.append(j)
    # print('search', search_L)
    search_L.pop(0)

true_ans = guiyi(answer)
print('找到答案了:',true_ans)
print(len(list2str(true_ans)))