"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.4
"""
import pandas as pd 

def preprocess_raw_data (heritage_foundation_database: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for heritage_foundation_data.

    Args:
        heritage_foundation_data: Raw data.
    Returns:
        Preprocessed data with:
           null rows deleted, 
           replace 'The Bahamas' for 'Bahamas' to match the data,
           deleting columns with lots of null,
           substitute null values for 0,
           rename columns,
           substitute space for underline and lower case.
    """     
    pp_data = heritage_foundation_database.dropna(axis=0, subset=["Overall Score"])
    pp_replace_name = pp_data.replace('The Bahamas','Bahamas',regex=True)
    pp_drop_columns = pp_replace_name.drop(axis=1, columns=["Judicial Effectiveness", "Fiscal Health"])
    pp_na_fill = pp_drop_columns.fillna(value={"Labor Freedom": 0})
    preprocess_data = pp_na_fill.rename(columns={
        "Name": "country",
        "Index Year": "year",
        "Overall Score": "score",
        "Property Rights": "property_right",
        "Government Integrity": "government_integrity",
        "Tax Burden": "tax_burden",
        "Government Spending": "government_spending",
        "Business Freedom": "business_freedom",
        "Labor Freedom": "labor_freedom",
        "Monetary Freedom": "monetary_freedom",
        "Trade Freedom": "trade_freedom",
        "Investment Freedom": "investment_freedom",
        "Financial Freedom": "financial_freedom"
        })
    preprocess_data['country'] = preprocess_data['country'].replace(' ','_',regex=True).str.lower()
    return preprocess_data


def preprocess_world (world_database: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for world_data.

    Args:
        world_data: Raw data.
    Returns:
        Preprocessed data with:
           selecting only the necessary columns,
           substitute space for underline and lower case.
    """     
    preprocess_world_data = world_database[["country", "region"]]

    preprocess_world_data['region'] = preprocess_world_data['region'].replace(' ','_',regex=True).str.lower()
    
    preprocess_world_data['country'] = preprocess_world_data['country'].replace(' ','_',regex=True).str.lower()
    
    return preprocess_world_data
