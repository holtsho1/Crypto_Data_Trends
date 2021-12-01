from CMCAPI_Data_Pull import *
#from New_Crypto_24H_GainsVsLosses import *
#from Sniper import *
import requests
import lxml.html

USDInvestment=50 #in US dollars
TrailingStopLoss=30 #in percent
html = requests.get('https://coinmarketcap.com/currencies/binance-coin/')
doc = lxml.html.fromstring(html.content)
BNBPrice=doc.xpath('//*[@id="__next"]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span/text()')
BNBPrice=BNBPrice[0]
BNBPrice=BNBPrice.strip("$")
BNB_amount=USDInvestment/float(BNBPrice)
#requests CMC API data based on CMC API DATA CMCAPI_Data_Pull
data_request=CMCAPI_DataExtract()
#create method to hold data request to compare against new pull??
time.sleep(5)
new_data_request=CMCAPI_DataExtract()
#uses CMC API DATA to compare recently added cryptos between newest data pull and last data pull
#for loop iterates through latest 30 added and finds all cryptos added since last data pull
#will find token address from API data and call sniper bot if cryptos in newest data pull don't match last data pull
for i in range(0,30):
    if not new_data_request['data'][i]['name']==data_request['data'][0]['name']:
        if new_data_request['data'][i]['platform']['name']=='Binance Smart Chain (BEP20)':
            #token address pulled from data
            token_address=new_data_request['data'][i]['platform']['token_address']
            #trigger sniper bot
            #Example: python Sniper.py -t <TOKEN_ADDRESS> -a <AMOUNT> -tx <TXAMOUNT> -hp -wb <BLOCKS WAIT BEFORE BUY> -tp <TAKE PROFIT IN PERCENT> -tsl <TRAILING STOP LOSE IN PERCENT>
            #Example: python Sniper.py -t 0x34faa80fec0233e045ed4737cc152a71e490e2e3 -a 0.001 -tx 2 -hp  -wb 10 -tp 50
            SniperBot().StartUP('-t '+token_address+' -a '+BNB_amount[0]+' -tsl '+TrailingStopLoss)  #needs debugging??
        #print(new_data_request['data'][0]['name'],data_request['data'][0]['name'],'if')  #troubleshooting statement
        else:
            #breaks for loop once all cryptos that have been added are found
            break
    else:
        #breaks the for loop if no cryptos were added
        #print('its a match maury') #troubleshooting statement
        break
