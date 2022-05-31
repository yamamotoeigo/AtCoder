a, b, c = map(int, input().split())
list = [a,b,c]
list.sort()
if b == list[1]:
    print("Yes")
else:
    print("No")