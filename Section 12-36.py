import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#print(1*2*3*4)
#print(1*2*3*4*5*6*7)

logging.disable(logging.CRITICAL) #you can use this logging method to disable all logging messages at critical or higher

logging.debug('Start of Program.')

def factorial(n):
    logging.debug('start of factorial.')
    total = 1
    for i in range(1, n+1): #Range begins at 0 unless you tell it otherwise
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

        logging.debug('Return Values is %s' % (total))
    return total

print(factorial(5))
logging.debug('End of program.')