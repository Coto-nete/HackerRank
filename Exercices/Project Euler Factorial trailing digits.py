def fac(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def convert(number, base):
    if number < base:
        return str(number)
    else:
        return convert(number // base, base) + str(number % base)

inputa = list(map(str, input().split()))
if inputa[0].isalpha():
    inputa[0] = str(ord(inputa[0]) - 54)

for _ in range(int(inputa[1])):
    number = int(input())
    result = convert(fac(number), int(inputa[0]))
    print(result.rstrip('0')[-5:])
