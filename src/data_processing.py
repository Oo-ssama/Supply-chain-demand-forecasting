import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding="ISO-8859-1")
    df['date'] = pd.to_datetime(df['shipping date (DateOrders)'])
    return df

def build_weekly_demand(df, product_name):
    df_product = df[df['Product Name'] == product_name]
    weekly_demand = (
        df_product
        .groupby(pd.Grouper(key='date', freq='W'))
        .size()
        .reset_index(name='demand')
    )
    return weekly_demand

