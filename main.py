import get_data as gd
import read_data as rd
import plot


import os
import sys
#import threading

Error1 = '\nError: Unable to create threads.'
Error2 = '\nError: Unable to initialize threads.'

def work1():
    i = 0
    urlINFO = list()
    
    if os.path.exists('Data') != True:
        os.system('mkdir Data')
    
    while True:
        urlINFO = gd.get_url(i)
        if urlINFO[0] == False:
            break
        gd.readWrite_url_data(urlINFO)
        i = i + 1

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