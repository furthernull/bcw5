dividend = int(input())
divisor = int(input())
nextMult = None

if divisor < 0:
    divisor *= -1

nextMult = dividend - (dividend % divisor)

if nextMult < dividend:
    nextMult += divisor

print(nextMult)
