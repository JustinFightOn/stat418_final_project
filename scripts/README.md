# Server

This folder contains information about the server. 

The `prediction.py` contains the Python code that pulls data from alphavantage api, transform the data from JSON to dataframe, and predicts stock price using the auto.arima method.

The `server.py` contains code that determines the method behavious of `GET` and `POST`. It receives a requests with JSON data, utilizes the `prediction.py` to make the prediction, and returns result in JSON format.

The `api_key.txt` is the api_key for the alphavantage api.