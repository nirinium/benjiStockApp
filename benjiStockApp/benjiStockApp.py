import csv
import time

import requests

import pandas as pd
import plotly
import PIL
from PIL import Image, ImageDraw, ImageFont
import os
import pathlib

def drawTicker():
    im = Image.new('RGBA', (100,300), 'white')
    draw = ImageDraw.Draw(im)
    draw.text((20, 150), 'Hello', fill='purple')
    im.save('\\ticker.png')
    
drawTicker()

def mainF():
    # Request sent for while loop
    r = requests.get("https://finance.yahoo.com/quote/%5EDJI/components/")

# While the website request is "OK"
    if (r.status_code == 200):
        # Grabs the table data from the website and parses
        stocks = pd.read_html("https://finance.yahoo.com/quote/%5EDJI/components/", header=0, parse_dates=["Symbol"])
        df = pd.DataFrame(stocks)
        cwd = os.getcwd()
        df.to_csv('test.csv')
        print(stocks[0])

    drawTicker()

mainF()

exit()