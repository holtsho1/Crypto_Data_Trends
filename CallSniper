#call sniper bot

SniperBot().Startup()

#Example: python Sniper.py -t <TOKEN_ADDRESS> -a <AMOUNT> -tx <TXAMOUNT> -hp -wb <BLOCKS WAIT BEFORE BUY> -tp <TAKE PROFIT IN PERCENT> -sl <STOP LOSE IN PERCENT>
#Example: python Sniper.py -t 0x34faa80fec0233e045ed4737cc152a71e490e2e3 -a 0.001 -tx 2 -hp  -wb 10 -tp 50

###*'-t' or '--token', Token for snipe e.g. "-t 0x34faa80fec0233e045ed4737cc152a71e490e2e3"
#'-a' or '--amount', float, Amount in Bnb to snipe e.g. "-a 0.1"

#'-tx' or '--txamount', how mutch tx you want to send? It split your BNB amount in e.g. "-tx 5"

#'-wb' or '--awaitBlocks', default=0, Await Blocks before sending BUY Transaction. e.g. "-ab 50"

#'-hp' or '--honeypot', if you use this Flag, your token get checks if token is honypot before buy!

#'-nb' or '--nobuy', No Buy, Skipp buy, if you want to use only TakeProfit/StopLoss/TrailingStopLoss
#'-tp' or '--takeprofit', Percentage TakeProfit from your input BNB amount. e.g. "-tp 50"
#'-tsl'or '--trailingstoploss', 'Percentage Trailing-Stop-loss from your first Quote "-tsl 50"

#'-so' or '--sellonly', Sell ALL your Tokens from given token address
#'-bo' or '--buyonly', Buy Tokens with your given amount

#* = require every time its runs!

python sniper.py '-t '+token_address+' -a '+BNB_amount+' -tp '+take_profit+' -tsl '+trailing_stop_loss
