import get_info as gi
import read_data as rd
import plot


import os
import sys
#import threading

Error0 = '\nError: No Url file exists'
Error1 = '\nError: Unable to create threads.'
Error2 = '\nError: Unable to initialize threads.'

def work1():
    print('''To scrap data from internet Create a txt file name with key.txt
         and put kwywords and links each with new line character "\n"/enter''')
    if os.path.exist('key.txt') == True:
        with open('key.txt', 'w+') as fp:
            wordds = []
            while(True)
                temp = temp + fp.read(1)
                if temp[len(temp) - 1] == '\n':
                    words.append(temp)
                elif temp[len(temp) - 1] = '':
                    break
            infObj = gi.initialize(words)

def work2():
    pass

def start():
    #try:
        #t1 = threading.Thread(target=work1, args=("Thread-1"))
    work1()
        #work2()
    #except:
        #sys.exit(Error1)
      
    '''  
    try:
        t1.start()
    except:
        sys.exit(Error2)
    '''

#execution of programm will start from here
start()
