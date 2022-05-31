import sys
sys.setrecursionlimit(500000)

def input():
    return sys.stdin.readline()[:-1]

a, b = map(int, input().split())
x = [list(input().split()) for i in range(a)]
pos = []
yPosList = []
xPosList = []

for row in range(len(x)):
    for col in range(len(x[row])):
            # print(x[row][col]) 
            # print((x[row][col]).find("o"))
            pos.append((x[row][col]).find("o"))
            
print(pos)
for i in range(len(pos)):
    if pos[i] != -1:
        yPosList.append(i)
        xPosList.append(pos[i])

# oが出るときのそれぞれのx座標
# print(xPosList)
# oが出るときのそれぞれのy座標
# print(yPosList)

# 答えは |xPos1 - xPos2|+|yPos1 - yPos2|
ans = abs(xPosList[1] - xPosList[0]) + abs(yPosList[1] - yPosList[0])
print(ans)