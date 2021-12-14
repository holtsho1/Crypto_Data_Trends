#https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
#-----------------------------------------------------------------------
# import time
# from datetime import datetime
# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# import json
# from datetime import date
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'fc955bba-050a-4a38-b597-958cb8fb8573',
}
