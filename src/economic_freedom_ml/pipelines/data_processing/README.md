# Pipeline data_processing

> *Note:* This is a `README.md` boilerplate generated using `Kedro 0.18.4`.

## Overview

This pipeline preprocesses raw data from two sources: the Heritage Foundation and a world database. The preprocessing involves cleaning, transforming, and preparing the data for further analysis and modeling. Specifically, it handles missing values, renames columns, and formats data to ensure consistency.

### Nodes

1. **preprocess_raw_data_node**
    - **Function:** `preprocess_raw_data`
    - **Description:** Preprocesses the Heritage Foundation database by:
        - Deleting null rows based on the "Overall Score".
        - Replacing 'The Bahamas' with 'Bahamas' to standardize country names.
        - Dropping columns with many null values.
        - Substituting null values in the "Labor Freedom" column with 0.
        - Renaming columns for clarity and consistency.

2. **preprocess_world_data_node**
    - **Function:** `preprocess_world`
    - **Description:** Preprocesses the world database by:
        - Selecting only the necessary columns ("country" and "region").
        - Replacing spaces with underscores and converting text to lowercase in the "country" and "region" columns.

## Pipeline inputs

1. **heritage_foundation_database**
    - **Description:** Raw data from the Heritage Foundation containing various economic indicators for different countries.
    - **Type:** `pandas.DataFrame`

2. **world_database**
    - **Description:** Raw data containing country and region information.
    - **Type:** `pandas.DataFrame`

## Pipeline outputs

1. **preprocess_data**
    - **Description:** Preprocessed Heritage Foundation data ready for analysis.
    - **Type:** `pandas.DataFrame`

2. **preprocess_world_data**
    - **Description:** Preprocessed world database with formatted country and region names.
    - **Type:** `pandas.DataFrame`
