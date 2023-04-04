import pandas as pd
import os
import time

def CheckLogs():
    if os.path.exists('logs/logs.csv') == False:
        os.system('mkdir logs')
        fp = open('logs/logs.csv', 'w')
        fp.write('"User","LogIn","LogOut","Errors"\n')
        fp.close()
    def SaveLogs():
        with pd.read_csv('logs/logs.csv') as df:
            log = pd.DataFrame({"User": os.getlogin(), "LogIn": time.ctime(time.time()), "LogOut": None, "Errors": None})
            log.to_csv('logs/logs.csv', index = False)
    def ProgramEndLogs():
        with pd.read_csv('logs/logs.csv') as df:
            df['LogOut'][len(df.columns) - 1] = time.ctime(time.time())
    def ErrorLogs(error):
        with pd.read_csv('logs/logs.csv') as df:
            df['errors'][len(df.columns) - 1] = error
        
