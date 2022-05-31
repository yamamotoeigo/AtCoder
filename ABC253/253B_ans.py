from cmath import pi


h, w = map(int, input().split())
s = [input() for _ in range(h)]
# print(s)
# print(s[0][1])
pieces = []
for i in range(h):
  for j in range(w):
    if s[i][j] == 'o':
      pieces.append((i, j))
print(pieces)
a, b = pieces[0]
c, d = pieces[1]
print(abs(a - c) + abs(b - d))
