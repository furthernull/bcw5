x = int(input())
y = int(input())
z = int(input())

if x + y > z:
    print('alpha')
elif y - z > x:
    print('bravo')
elif y % z == 0:
    print('charlie')
else:
    print('zulu')