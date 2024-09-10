import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly

data = pd.read_csv("stock_data.csv")

data = data[["Date", "Close"]]

data.columns = ["ds", "y"]

prophet = Prophet(daily_seasonality=True)
prophet.fit(data)

future_dates = prophet.make_future_dataframe(periods=365)
predictions = prophet.predict(future_dates)

plot_plotly(prophet, predictions) 