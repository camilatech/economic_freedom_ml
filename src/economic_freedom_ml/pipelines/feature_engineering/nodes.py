"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""
import pandas as pd

def creating_features (preprocess_data: pd.DataFrame, preprocess_world_data: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for world_data.

    Args:
        preprocess_data: preprocessed data from heritage fundation.
        preprocess_world_data: prepossed data with countries and its continents.

    Returns:
        Data with new features:
           Joining both dataframes and creating dummies.
    """   
    filtered_data = preprocess_data[['country', 'year', 'score']]
    
    data_with_continents = pd.merge(
        filtered_data, 
        preprocess_world_data,
        how="left",
        on='country', 
    )

    data_with_features = pd.get_dummies(data_with_continents, columns=['country', 'region'], prefix='', prefix_sep='')

    return data_with_features

def creating_feature_prophet (preprocess_data: pd.DataFrame, preprocess_world_data: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for world_data.

    Args:
        preprocess_data: preprocessed data from heritage fundation.
        preprocess_world_data: prepossed data with countries and its continents.

    Returns:
        Data with new features:
           Joining both dataframes and creating dummies.
    """   
    filtered_data = preprocess_data[['country', 'year', 'score']]
    
    data_with_continents = pd.merge(
        filtered_data, 
        preprocess_world_data,
        how="left",
        on='country', 
    )

    data_for_prophet = data_with_continents.rename({'year': 'ds', 'score':'y','Country':'country'},axis=1)

    data_for_prophet['ds'] = (data_for_prophet['ds'].map(str)+ "-12-31")

    data_for_prophet['ds'] = pd.to_datetime(data_for_prophet['ds'])

    return data_for_prophet