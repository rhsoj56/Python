#import libraries

from ftplib import FTP

#function called checker which will test user/password against FTP

def checker():
    try:
        ftp = FTP(input("Enter an IP address: "))
        ftp.login() #login with anonymous creds
        ftp.retrlines('LIST') #list directories
    except:
        print("FTP Anonymous access denied!")
        
checker()