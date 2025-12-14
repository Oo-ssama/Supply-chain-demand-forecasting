from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.arima.model import ARIMA

def naive_forecast(series, horizon):
    return [series.iloc[-1]] * horizon

def ses_forecast(series, horizon):
    model = SimpleExpSmoothing(series).fit()
    return model.forecast(horizon)

def arima_forecast(series, horizon):
    model = ARIMA(series, order=(1,1,1))
    fitted = model.fit()
    return fitted.forecast(horizon)

