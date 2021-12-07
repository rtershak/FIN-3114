import yfinance as yf
import pandas_datareader as web
from datetime import datetime, timedelta
import pandas
import matplotlib.pyplot as plt
from Callable_lists_1 import Ticker_list, Date_list, validNames, Names
import numpy as np

# Times= [2,5,21,126,254]
dayAvg=0
weekAvg=0
monthAvg=0
biannualAvg=0
annualAvg=0
Hugeset=[]
for t in range(validNames):
    Start = datetime.strptime(Date_list[t], "%Y-%m-%d")
    End = Start +timedelta(days=600)
    df = yf.download(Ticker_list[t], source_data = 'yahoo', start = Start, end = End)
    x = df['Close']
    a = np.array(x)
    b=a[0:1:]
    day = ((a[1:2:]/b)-1)
    dayAvg+=day
    week = ((a[4:5:]/b)-1)
    weekAvg+=week
    month = ((a[20:21:]/b)-1)
    monthAvg+=month
    bi = ((a[125:126:]/b)-1)
    biannualAvg+=bi
    ann = ((a[253:254:]/b)-1)
    annualAvg+=ann
    l= 1
    m=2
    singles=[]


dayAvg/=validNames
weekAvg/=validNames
monthAvg/=validNames
biannualAvg/=validNames
annualAvg/=validNames

print(dayAvg)
print(weekAvg)
print(monthAvg)
print(biannualAvg)
print(annualAvg)



