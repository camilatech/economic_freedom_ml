# Pipeline data_science

> *Note:* This is a `README.md` boilerplate generated using `Kedro 0.18.4`.

## Overview

This pipeline fits a Prophet model to predict economic freedom scores for Mercosur countries. The model is trained on historical data and makes future predictions, which are then filtered to include only Mercosur countries. 

### Nodes

1. **mercosur_predictions_node**
    - **Function:** `fit_model`
    - **Description:** Fits the Prophet model to historical economic freedom data for each country, makes future predictions, and filters the predictions to include only Mercosur countries.

## Pipeline inputs

1. **data_for_prophet**
    - **Description:** Preprocessed data containing historical economic freedom scores with columns 'ds' (date), 'y' (value), and 'country'.
    - **Type:** `pandas.DataFrame`

## Pipeline outputs

1. **mercosur_predictions**
    - **Description:** Predictions of economic freedom scores for Mercosur countries.
    - **Type:** `pandas.DataFrame`
