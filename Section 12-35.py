'''

*************
*           *
*           *
*           *
*************

'''

import traceback
import os

def BoxPrint(symbol, width, height):

    if len(symbol) != 1:
        raise Exception('"symbol needs to be a string of lenght 1.')
    
    if (width<2) or (height<2):
        raise Exception('"width" and "heigh" must be greater or equal to 2')

    print(symbol * width)

    for i in range(height -2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

BoxPrint('*',1,5)
'''
try:
    raise Exception('This is an Error Message')
except:
    errorFile = open('error_Log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.write('\n')
    errorFile.close()
    print('The traceback info was written to error_log.txt in the working directory.')

print(os.getcwd())

#assert False, 'This is the error message.'

market_2nd = {'ns':'Green','ew':'Red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'Green':
            intersection[key] = 'Yellow'
        elif intersection[key] == 'Yellow':
            intersection[key] = 'Red'
        elif intersection[key] == 'Red':
            intersection[key] = 'Green'
#I assert, that this condition must always be true!
    assert 'Red' in intersection.values(), 'Neither Light is red!' + str(intersection)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
'''