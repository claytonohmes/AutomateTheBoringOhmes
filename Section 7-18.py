import pprint
# a dictonary describing a cat
cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}
# create a blank list for all cats
allCats = []
allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
allCats.append({'name': 'Fat-Tail', 'age': 5, 'color': 'gray'})
allCats.append({'name': '???', 'age': -1, 'color': 'orange'})

# this prints out the data structure containing dictonaries of the types of cats.
print(allCats)

theBoard = {'Top-L': ' ', 'Top-M': ' ', 'Top-R': ' ', 'Mid-L': ' ', 'Mid-M': ' ', 'Mid-R': ' ',\
            'Low-L': ' ', 'Low-M': ' ', 'Low-R': ' '}
pprint.pprint(theBoard)

theBoard['Mid-M'] = 'X'
theBoard['Top-L'] = 'X'
theBoard['Top-M'] = 'O'

pprint.pprint(theBoard)

def printBoard(Board):
    print(Board['Top-L'] + '|' + Board['Top-M'] + '|' + Board['Top-R'])
    print('-----')
    print(Board['Mid-L'] + '|' + Board['Mid-M'] + '|' + Board['Mid-R'])
    print('-----')
    print(Board['Low-L'] + '|' + Board['Low-M'] + '|' + Board['Low-R'])

printBoard(theBoard)

print(type(42))
print(type(theBoard))