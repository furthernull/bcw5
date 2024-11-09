x = int(input())
y = int(input())

if x > y:
    print('alpha')
elif x < 0 and y == 0:
    print('bravo')
elif x == 0 or y == 0:
    print('charlie')
else:
    print('zulu')