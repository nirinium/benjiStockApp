import requests
import time
import pandas as pd
#import PySimpleGUI as sg

#def GUI():
    #sg.PopupYesNo('Is this a popup?')

def mainF():
    #Request sent for while loop
    r = requests.get("https://finance.yahoo.com/quote/%5EDJI/components/")

    #While the website request is "OK"
    while (r.status_code==200):
	    #Grabs the table data from the website and parses
	    stocks = pd.read_html("https://finance.yahoo.com/quote/%5EDJI/components/", header=0, parse_dates=["Symbol"])
	    print(stocks[0])
	    #Set time for website refresh to update stock numbers
	    time.sleep(120)
mainF()
#Pressing Ctrl + C will stop the script from running
#GUI()
exit()
