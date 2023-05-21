"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.4
"""
import pandas as pd 
import xgboost as xgb
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from prophet import Prophet
from datetime import datetime

def fit_model (data_for_prophet: pd.DataFrame) -> pd.DataFrame:
    """Slip the data into train and test datasets
    """
    # Assuming your dataset is in a DataFrame called 'data', with columns 'ds', 'y', and 'country'
    countries = data_for_prophet['country'].unique()
    predictions = []

    for country in countries:
        # Filter data for the current country
        country_data = data_for_prophet[data_for_prophet['country'] == country]
        
        # Define and fit the model
        model = Prophet()
        model.fit(country_data)
        
        # Create a DataFrame for future dates
        future = model.make_future_dataframe(periods=5, freq='Y') # 5 years of daily predictions
        
        # Make predictions and store them in the 'predictions' list
        forecast = model.predict(future)
        forecast['country'] = country
        predictions.append(forecast)

    # Combine all predictions into a single DataFrame
    all_predictions = pd.concat(predictions, ignore_index=True)

    data_for_merge = data_for_prophet['country'].drop_duplicates()

    arranging_order = pd.merge(
        data_for_merge, 
        all_predictions,
        how="left",
        on=['country'], 
    )

    mercosur = ["argentina", "brazil", "paraguay", "uruguay", "bolivia", "chile", "colombia", "ecuador", "guyana", "peru", "suriname"]

    mercosur_predictions  = arranging_order[arranging_order["country"].isin(mercosur)]

    return mercosur_predictions