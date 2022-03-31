import pandas as pd
import numpy as np
from neuralprophet import NeuralProphet

def forecast(df,country="US"):
    m = NeuralProphet()
    m.add_country_holidays(country)
    m.fit(df)
    future = m.make_future_dataframe(df,periods=365,n_historic_predictions=True)
    forecast = m.predict(future)
    return forecast

