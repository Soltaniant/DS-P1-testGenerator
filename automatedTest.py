#only for cleaner output :)
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

#reading the text file:
file = open("texts/short.txt")
text = file.read()
words = text.split('\n')

'''
Paste your codes here:
Tree, Nodes and other functions
'''



#choose a random word
import random

def getARandomWord(words):
    return random.choice(words)

#conver the choosen word to a regex-like
def randomlyConvertToRegex(string:list):
    end = len(string)
    #choose a range in string(NOT VERY IMPORTANT!)
    startingIndex = random.randint(0, end)
    endingIndex = random.randint(startingIndex, end + (end - startingIndex) // 2)
    
    return replace(string, startingIndex, endingIndex + 1)

def replace(string, start, end):
    a = string[:start]
    b = string[end:]
    return [str(a) + '.*' + str(b), str(a) + '\S*' + str(b)] #we will need both formats

import re
#find result with regex
def findByRegex(word):
    for i in words:
        if re.match(r'\b'+ word + r'\b', i): yield i


#driver code:
TEST_TIMES = 10

for i in range(TEST_TIMES):
    query = randomlyConvertToRegex(getARandomWord(words))
    regex_result = findByRegex(query[0])

    #start time:
    import time
    startTime = time.time()
    

    '''call your main function here, between start and end time'''

    #end time
    executionTime = time.time() - startTime

    my_result = 'your result should be used here!'.split(' ') #list of answers! not the final string

    print('{: <15}'.format(query[0]), end="")
    if  set(regex_result) != set(my_result):
        print(f'{bcolors.FAIL}Missing words:{bcolors.ENDC}', set(regex_result).difference(set(my_result)))
    else:
        print(f'{bcolors.OKGREEN}Accepted{bcolors.ENDC} | {executionTime}')
        


