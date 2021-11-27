import time
from datetime import datetime
import requests
import lxml.html
import csv
while True:
    DayGains=0
    SumGains=0
    html = requests.get('https://coinmarketcap.com/new/')
    doc = lxml.html.fromstring(html.content)
    #add up total percent gains by all 30 new cryptos
    for i in range(1,30):
        #finds the absolute value percent day gains for this coin
        DayGains=doc.xpath('//*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr'+str([i])+'/td[6]/span/text()[1]')
        #finds whether the percentage is positive or negative
        PosOrNeg=doc.xpath('//*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr'+str([i])+'/td[6]/span/span/@class')
        #finds the type of parent chain (Binance, Ethereum, Tron, Avalanche) for this token
        ParentCoinType=doc.xpath('//*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr'+str([i])+'/td[9]/div/text()')
        if ParentCoinType=="Binance Coin":
            if PosOrNeg[0]=='icon-Caret-up':
                BSCSumGains=BSCSumGains+float(DayGains[0])
            else:
                BSCSumGains=BSCSumGains-float(DayGains[0])
        print(PosOrNeg)
        if PosOrNeg[0]=='icon-Caret-up':
            SumGains=SumGains+float(DayGains[0])
        else:
            SumGains=SumGains-float(DayGains[0])

    if SumGains>0:
        DayTrend="Positive"
        InvOpp='Average'
    if SumGains>50:
        DayTrend="Very Positive"
        InvOpp='Above Average'
    if SumGains>100:
        DayTrend="Hella Gains"
        InvOpp='Opportune Time'
    else:
        DayTrend="Negative"
        InvOpp="Don't invest"
    today=datetime.now()
    #below print statements used for startup / troubleshooting
    #print(SumGains)
    #print(DayTrend)
    #print(today)
    Data={'Total Gains':SumGains,'Binance Gains':BSCSumGains,'Trend':DayTrend,'Invest Rating':InvOpp,'Date':today}
    print(Data)
    with open(r'24HGainsVsLossesDataStore', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(Data)
    f.close()
    time.sleep(300)
