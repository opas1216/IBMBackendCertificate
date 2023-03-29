from pycoingecko import CoinGeckoAPI
import pandas as pd


cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
bitcoin_price_data = bitcoin_data['prices']
data = pd.DataFrame(bitcoin_data)
data_price = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
print(data.head(700))
print(data_price.head(700))
data_price['Date'] = pd.to_datetime(data_price['TimeStamp'], unit = 'ms')
print("Convert to DateTime\n")
print(data_price.head(700))

candlestick_data = data_price.groupby(data_price.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})
fig = go.Figure