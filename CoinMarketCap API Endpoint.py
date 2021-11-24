#https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
#-----------------------------------------------------------------------
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'fc955bba-050a-4a38-b597-958cb8fb8573',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  data=data.splitlines(True)
  print(data)    #prints a lot of data
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
