import numpy as np
from statsmodels.tsa.arima.model import ARIMA

#### Calculate the metrics RMSE and MAPE ####
def calculate_rmse(y_true, y_pred):
    """
    Calculate the Root Mean Squared Error (RMSE)
    """
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    return rmse


def calculate_mape(y_true, y_pred):
    """
    Calculate the Mean Absolute Percentage Error (MAPE) %
    """
    y_pred, y_true = np.array(y_pred), np.array(y_true)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return mape

def calculate_perf_metrics(y_true, y_pred):
    ### RMSE
    rmse = calculate_rmse(y_true, y_pred)
    ### MAPE
    mape = calculate_mape(y_true, y_pred)

    return rmse, mape

def make_model_predictions(train, forecast_size=7,
                            arima_order=(2,1,1), short_trend_window_size = 20, long_trend_window_size = 100): 
    """
    Calculate model predictions
    """

    train_returns = train[1:] / train[:-1] - 1
    avg_return_short = np.mean(train_returns[-short_trend_window_size:])
    avg_return_long = np.mean(train_returns[-long_trend_window_size:])

    short_trend_prediction = train[-1] * (1 + avg_return_short) ** np.arange(forecast_size + 1)
    long_trend_prediction = train[-1] * (1 + avg_return_long) ** np.arange(forecast_size + 1)

    # # fit ARIMA model
    model = ARIMA(train, order=arima_order, trend='t')
    model_fit = model.fit()
    model_forecast = model_fit.forecast(forecast_size)
    arima_prediction = np.concatenate((train[-1:], model_forecast))

    return short_trend_prediction, long_trend_prediction, arima_prediction