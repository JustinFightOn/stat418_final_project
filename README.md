# Stock Prediction API
This is an API using the auto.arima method in Python’s pmdarima  package to fit a ARIMA model with the best (lowest) AIC score on the univariate time series stock data of User's interest to predict the selected stock's next N (default 7) business days' daily high prices. The data is pulling alphavantage using a given API, which returns the last 100 days’ stock price of the selected stocks.

The model is written in Python, and it is wrapped in a docker container for reproduction purpose. Finally, it is hosted on an EC2 instance that everyone can access it.

To run this API, just open a new web page and paste the following address:

` http://ec2-54-153-4-11.us-west-1.compute.amazonaws.com:8000/ `

It should return:

`server is up - nice job!`

Finally, to get the stock predictions, here is sample input into the model:

`http://ec2-54-153-4-11.us-west-1.compute.amazonaws.com:8000/AMZN`

The result should be:

` {'Stock': 'AMZN', 'Last Refreshed': '2019-05-31', 'Previous Stock Price': {'2019-05-22': 1871.48, '2019-05-23': 1844.0, '2019-05-24': 1841.76, '2019-05-28': 1849.27, '2019-05-29': 1830.0, '2019-05-30': 1829.47, '2019-05-31': 1795.59}, 'Forecasted Stock Price': {'2019-06-03': 1799.46, '2019-06-04': 1806.91, '2019-06-05': 1806.2, '2019-06-06': 1802.54, '2019-06-07': 1805.27, '2019-06-10': 1810.43, '2019-06-11': 1810.59}}`

You can change the `AMZN` to any stocks of your choice, the followings are some famous stocks:

` GOOGL`, ` FB`, `AMZN`, ` AAPL`, `MSFT`, `ROKU`
