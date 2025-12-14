import streamlit as st
import matplotlib.pyplot as plt

from src.data_processing import load_data, build_weekly_demand
from src.forecasting import naive_forecast, ses_forecast, arima_forecast

st.title("Demand Forecasting – Supply Chain Project")

df = load_data("data/dataco.csv")

product = st.selectbox("Select a product", df['Product Name'].unique())

data = build_weekly_demand(df, product)
series = data['demand']

horizon = st.slider("Forecast horizon (weeks)", 4, 20, 8)

model = st.selectbox("Forecasting model", ["Naive", "SES", "ARIMA"])

if model == "Naive":
    forecast = naive_forecast(series, horizon)
elif model == "SES":
    forecast = ses_forecast(series, horizon)
else:
    forecast = arima_forecast(series, horizon)

st.subheader("Historical Demand")
fig, ax = plt.subplots()
ax.plot(series.values)
st.pyplot(fig)

st.subheader("Forecast")
fig2, ax2 = plt.subplots()
ax2.plot(range(len(series)), series.values, label="History")
ax2.plot(range(len(series), len(series)+horizon), forecast, label="Forecast")
ax2.legend()
st.pyplot(fig2)
