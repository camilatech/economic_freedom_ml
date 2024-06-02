# Pipeline data_engineering

> *Note:* This is a `README.md` boilerplate generated using `Kedro 0.18.4`.

## Overview

This pipeline is responsible for creating features from the preprocessed data. It combines data from the Heritage Foundation with country and region information, generating new features for modeling. The pipeline includes two nodes: one for general feature creation and another specifically for preparing data for the Prophet model.

### Nodes

1. **data_with_features_node**
    - **Function:** `creating_features`
    - **Description:** 
        - Joins preprocessed data with world data to add continent information.
        - Creates dummy variables for the `country` and `region` columns.
        - Outputs a dataframe with new features for modeling.

2. **data_for_prophet_node**
    - **Function:** `creating_feature_prophet`
    - **Description:** 
        - Joins preprocessed data with world data to add continent information.
        - Renames columns and formats the date for the Prophet model.
        - Outputs a dataframe specifically formatted for Prophet.

## Pipeline inputs

1. **preprocess_data**
    - **Description:** Preprocessed data from the Heritage Foundation containing economic freedom scores.
    - **Type:** `pandas.DataFrame`

2. **preprocess_world_data**
    - **Description:** Preprocessed data containing countries and their corresponding regions.
    - **Type:** `pandas.DataFrame`

## Pipeline outputs

1. **data_with_features**
    - **Description:** Dataframe with new features, including dummy variables for countries and regions, ready for general modeling.
    - **Type:** `pandas.DataFrame`

2. **data_for_prophet**
    - **Description:** Dataframe formatted for the Prophet model, including date and score columns.
    - **Type:** `pandas.DataFrame`
