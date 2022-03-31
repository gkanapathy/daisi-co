import pandas as pd
import numpy as np
from prophet import Prophet

def forecast(df):
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=365,include_history=True)
    forecast = m.predict(future)
    return forecast
