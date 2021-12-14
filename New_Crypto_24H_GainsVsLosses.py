import time
from datetime import datetime
import requests
import lxml.html
import csv
from CoinMarketCap_API_Endpoint import *
while True:
    DayGains=0
    SumGains=0
    BSCSumGains=0
    try:
        html = requests.get('https://coinmarketcap.com/new/')
        doc = lxml.html.fromstring(html.content)
    except ConnectionError:
        print('Connection Error. Retrying in 5 seconds')
        time.sleep(5)
        continue
    except socket.gaierror:
        print('socket.gaierror. Retrying in 2 seconds')
        time.sleep(2)
        pass
    except NewConnectionError:
        print('NewConnectionError. Retrying in 2 seconds')
        time.sleep(2)
        pass
    except MaxRetryError:
        print('MaxRetryError. Attempting to reconnect in 10 seconds')
        time.sleep(10)
        continue
    #add up total percent gains by all 30 new cryptos
    for i in range(1,30):
        #finds the absolute value percent day gains for this coin
        DayGains=doc.xpath('//*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr'+str([i])+'/td[6]/span/text()[1]')
        #finds whether the percentage is positive or negative
        PosOrNeg=doc.xpath('//*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr'+str([i])+'/td[6]/span/span/@class')
        #finds the type of parent chain (Binance, Ethereum, Tron, Avalanche) for this token
        ParentCoinType=doc.xpath('//*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr'+str([i])+'/td[9]/div/text()')
        try:
            #print(ParentCoinType[0])
            if ParentCoinType[0]=="Binance Coin":
                if PosOrNeg[0]=='icon-Caret-up':
                    BSCSumGains=BSCSumGains+float(DayGains[0])
                else:
                    BSCSumGains=BSCSumGains-float(DayGains[0])
        except IndexError:
            pass
        #print(PosOrNeg)
        #print(BSCSumGains)
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

    if BSCSumGains>0:
        BSCDayTrend="Positive"
        BSCInvOpp='Average'
    if SumGains>50:
        BSCDayTrend="Very Positive"
        BSCInvOpp='Above Average'
    if SumGains>100:
        BSCDayTrend="Hella Gains"
        BSCInvOpp='Opportune Time'
    else:
        BSCDayTrend="Negative"
        BSCInvOpp="Don't invest"
    today=datetime.now()
    #below print statements used for startup / troubleshooting
    #print(SumGains)
    #print(DayTrend)
    #print(today)
    #Data={'Total Gains':SumGains,'Binance Gains':BSCSumGains,'Trend':DayTrend,'Invest Rating':InvOpp,'Date':today}
    OverallData=[SumGains,DayTrend,InvOpp,today]
    BSCData=[BSCSumGains,BSCDayTrend,BSCInvOpp,today]
    print(OverallData)
    with open(r'24HGainsVsLossesDataStore.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(OverallData)
    f.close()
    with open(r'24HGainsVsLossesDataStoreBSC.csv', 'a', newline='') as BSCf:
        writer = csv.writer(BSCf)
        writer.writerow(BSCData)
    BSCf.close()
    BSCSumGains=0
    time.sleep(300)
