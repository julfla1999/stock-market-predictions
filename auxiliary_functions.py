import matplotlib.pyplot as plt
import pandas as pd
from models_funtions import calculate_perf_metrics

def make_plot(history_data, history_dates, 
              predictions, prediction_dates, 
              forecasts, forecast_dates):

    short_trend_prediction, long_trend_prediction, arima_prediction = predictions
    short_trend_forecast, long_trend_forecast, arima_forecast = forecasts

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(history_dates, history_data, color='black', label='Rzeczywisty kurs')
    ax1.plot(prediction_dates, short_trend_prediction, label='Prognoza wg 20 dniowego trendu',
            color='blue', linestyle='--', linewidth=2)
    ax1.plot(prediction_dates, long_trend_prediction, label='Prognoza wg 100 dniowego trendu',
            color='green', linestyle='--', linewidth=2)
    ax1.plot(prediction_dates, arima_prediction, label='Prognoza wg ARIMA',
            color='red', linewidth=2)
    ax1.set_title('Prognozy na danych historycznych')
    #ax1.legend()

    ax2.plot(history_dates, history_data, color='black', label='Rzeczywisty kurs')
    ax2.plot(forecast_dates, short_trend_forecast, label='Prognoza wg 20 dniowego trendu',
            color='blue', linestyle='--', linewidth=2)
    ax2.plot(forecast_dates, long_trend_forecast, label='Prognoza wg 100 dniowego trendu',
            color='green', linestyle='--', linewidth=2)
    ax2.plot(forecast_dates, arima_forecast, label='Prognoza wg ARIMA',
            color='red', linewidth=2)
    ax2.set_title('Prognozy w przyszłość')
    ax2.legend()
    plt.savefig('prediction_forecast_plot')

    plt.show()

def save_forecast(forecasts, forecast_dates):

    short_trend_forecast, long_trend_forecast, arima_forecast = forecasts
    res_forecasts = pd.DataFrame({'short_trend': short_trend_forecast,
                            'long_trend': long_trend_forecast,
                            'arima': arima_forecast}, index=forecast_dates)
    
    res_forecasts.to_csv('forecasts.csv')

    print('Models forecasts: ')
    print(res_forecasts)

def save_prediction_summary(predictions, test):

    short_trend_prediction, long_trend_prediction, arima_prediction = predictions
    short_results = calculate_perf_metrics(test, short_trend_prediction[1:])
    long_results = calculate_perf_metrics(test, long_trend_prediction[1:])
    arima_results = calculate_perf_metrics(test, arima_prediction[1:])

    test_perfomance = pd.DataFrame({'short_trend': short_results,
                            'long_trend': long_results,
                            'arima': arima_results}, index=['RMSE', 'MAPE'])

    test_perfomance.to_csv('prediction_summary.csv')
    print("Wyniki modeli na zbiorze testowym:")
    print(test_perfomance)