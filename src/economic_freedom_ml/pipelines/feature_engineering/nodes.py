"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""
import pandas as pd

def creating_features (preprocess_data: pd.DataFrame, preprocess_world_data: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for world_data.

    Args:
        preprocess_data: preprocessed data from heritage fundation.
        preprocess_world_data: prepossed data with countries and its continents in dummy.

    Returns:
        Data with new features:
           Joining both dataframes.
    """   
    data_with_continents = pd.merge(
        preprocess_data, 
        preprocess_world_data,
        how="left",
        on='country', 
    )

    data_with_features = pd.get_dummies(data_with_continents, columns=['country'])

    return data_with_features