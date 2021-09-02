import sys

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return int(number)
    elif number % 2 == 1:
        number = 3 * number + 1
        return int(number)

try:
    while True:
        try:
            prompt = int(input())
            print(collatz(prompt))
        except ValueError:
            print('Non-int entered')


except KeyboardInterrupt:
    sys.exit()