import warnings
warnings.simplefilter('ignore')

import pandas as pd
import numpy as np
from models_funtions import make_model_predictions
from auxiliary_functions import save_prediction_summary, save_forecast, make_plot
from data_api_functions import ask_for_ticker, download_data

train_size = 300
forecast_size = 14

if __name__ == "__main__":

    #ticker = ask_for_ticker()
    #stockprices = download_data(ticker)

    stockprices = pd.read_csv("tsco.csv", index_col="timestamp")
    stockprices.sort_values(by=['timestamp'], inplace=True)
    stockprices.index = pd.to_datetime(stockprices.index)

    data = stockprices[-train_size:]
    dates = data.index
    forecast_dates = pd.date_range(start=dates[-1], periods=forecast_size + 1)
    prediction_dates = dates[-(forecast_size+1):]

    train = np.array(data[:-forecast_size]["close"])
    test = np.array(data[-forecast_size:]["close"])

    predictions = make_model_predictions(train, forecast_size=forecast_size)
    save_prediction_summary(predictions, test)

    forecasts = make_model_predictions(np.array(data['close']), forecast_size=forecast_size)
    save_forecast(forecasts, forecast_dates)
    make_plot(data[-50:]['close'], dates[-50:], 
              predictions, prediction_dates,
              forecasts, forecast_dates)
