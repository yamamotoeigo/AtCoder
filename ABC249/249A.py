A, B, C, D, E, F, X = map(int, input().split())
ans1 = (X - C)*A
ans2 = (X - F)*B
if ans1 == ans2:
    print("Draw")
elif ans1 > ans2:
    print("Takahashi")
else:
    print("Aoki")