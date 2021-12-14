from CoinMarketCap_API_Endpoint import *
def CMCAPI_DataExtract():
    session = Session()
    session.headers.update(headers)
    parameters = {
      #'start':'1',
      'limit':'30',
      'convert':'USD',
      'sort':'date_added',
      'sort_dir':'desc'
    }
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #data=data.splitlines(True)
      print('Data collected')    #prints a lot of data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

    return data
