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
        DayGains=doc.xpath('//*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr'+str([i])+'/td[6]/span/text()[1]')
        PosOrNeg=doc.xpath('//*[@id="__next"]/div/div/div[2]/div/div[2]/table/tbody/tr'+str([i])+'/td[6]/span/span/@class')
        print(PosOrNeg)
        if PosOrNeg[0]=='icon-Caret-up':
            SumGains=SumGains+float(DayGains[0])
        else:
            SumGains=SumGains-float(DayGains[0])

    if SumGains>0:
        DayTrend="Positive"
    if SumGains>50:
        DayTrend="Very Positive"
    if SumGains>100:
        DayTrend="Hella Gains"
    print(SumGains)
    print(DayTrend)
    today=datetime.now()
    print(today)
    Data=[SumGains,DayTrend,today]
    with open(r'24HGainsVsLossesDataStore', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(Data)
    f.close()
    time.sleep(300)
