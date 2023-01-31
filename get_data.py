import pandas as pd
import requests as rq

Error3 = '\nError: Unable establish connection, check your internet connection.'

def get_url(i):
    fmt = '' #save data in format in which the url recieeves
    url = '' #saves url
    
    #read no, url and format
    urlDF = pd.read_csv('urls.csv')
    
    if i+1 > len(urlDF):
        return [False]
    
    url = urlDF['Urls'][i]
    fmt = urlDF['Format'][i]
    
    return [True, i, url, fmt]
    
def readWrite_url_data(urlINFO):
    data = ''
    try:
        data = rq.get(urlINFO[2]) #get the data from url
    except:
        print(Error3)
    
    if data != '':
        saveData = open(f'Data/link{urlINFO[1]}Data.{urlINFO[3]}','w') #open file in a appropriate extension(given in urlINFO)
        saveData.write(data.text)