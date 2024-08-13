def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('You Tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) < 0:
        raise ValueError ("This is not a positive number")
    elif int(numCats) >= 4:
        print('Thats a lot of cats')
    else:
        print('that is not that many cats')
except ValueError:
    print('System Error: Please try inputing a number.')