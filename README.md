# Supply-chain-demand-forecasting
**Final Project – Advanced Statistics**  
Montpellier Business School  

---

##  Project Overview

This project focuses on **demand forecasting in a supply chain context** using real transactional data.  
The objective is to construct a demand signal from raw order data and evaluate the performance of classical **time-series forecasting models**.

The project combines:
- Supply Chain Analytics
- Statistical Forecasting
- Python Programming
- Interactive Visualization with Streamlit

---

##  Dataset Description

The dataset used is the **DataCo Supply Chain Dataset**, which contains **180,560 transactional records** from an international sporting goods supply chain.

Each transaction includes information on:
- Orders and customers
- Products and categories
- Sales and profit metrics
- Shipping and delivery dates
- Logistics and routing details

Since explicit demand quantities are not directly available, **demand is constructed by aggregating transactional orders over time**, which is a common practice in empirical supply chain research.

---

## Research Questions

This project aims to answer the following research questions:

1. How can transactional supply chain data be transformed into a meaningful demand signal?
2. Which time-series forecasting methods provide the best demand forecast accuracy?
3. What are the managerial implications of forecasting accuracy for supply chain planning?

---

## Methodology

### 1. Data Processing
- Data cleaning and date conversion
- Product-level filtering
- Weekly aggregation of transactional data to construct demand

### 2. Forecasting Models
The following forecasting models are implemented and compared:
- Naïve Forecast
- Simple Exponential Smoothing (SES)
- ARIMA (AutoRegressive Integrated Moving Average)

### 3. Evaluation Metrics
Forecasting performance is evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

---

##  Streamlit Application

An interactive **Streamlit dashboard** is developed to:
- Select products dynamically
- Visualize historical demand
- Generate forecasts
- Compare forecasting models visually

### ▶ Run the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

##  Project Structure

```
Supply-chain-demand-forecasting/
│
├── data
├── src/
│   ├── data_processing.py
│   ├── forecasting.py
│   └── evaluation.py
│
├── app.py
├── requirements.txt
├── README.md
```

---

## Research Papers (Inspiration)

1. **Lee, H. L., Padmanabhan, V., & Whang, S. (1997)**  
   *The Bullwhip Effect in Supply Chains*  
   MIT Sloan Management Review  
   https://sloanreview.mit.edu/article/the-bullwhip-effect-in-supply-chains/

2. **Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2018)**  
   *Statistical and Machine Learning Forecasting Methods: Concerns and Ways Forward*  
   International Journal of Forecasting  
   https://doi.org/10.1016/j.ijforecast.2018.01.001

3. **Hyndman, R. J., & Athanasopoulos, G. (2018)**  
   *Forecasting: Principles and Practice (3rd ed.)*  
   https://otexts.com/fpp3/

---

##  Academic Context

This project was developed as part of the **Advanced Statistics course**  
within the **Master in Supply Chain Management** at **Montpellier Business School**.

---

## 👤 Author

Student: *Oussama KASSIMI @ Houssama Tachihante*

Program: Master in Supply Chain Management  
Institution: Montpellier Business School
