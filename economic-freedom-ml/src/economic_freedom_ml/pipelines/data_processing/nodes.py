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
           rename columns.
    """     
    pp_data = heritage_foundation_database.dropna(axis=0, subset=["Overall Score"])
    preprocess_data = pp_data.rename(columns={
        "Name": "country",
        "Index Year": "year",
        "Overall Score": "score",
        "Property Rights": "property_right",
        "Government Integrity": "government_integrity",
        "Judicial Effectiveness": "judicial_effectiveness",
        "Tax Burden": "tax_burden",
        "Government Spending": "government_spending",
        "Fiscal Health": "fiscal_health",
        "Business Freedom": "business_freedom",
        "Labor Freedom": "labor_freedom",
        "Monetary Freedom": "monetary_freedom",
        "Trade Freedom": "trade_freedom",
        "Investment Freedom": "investment_freedom",
        "Financial Freedom": "financial_freedom"
        })
    return preprocess_data


def preprocess_world (world_database: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for world_data.

    Args:
        world_data: Raw data.
    Returns:
        Preprocessed data with:
           selecting only the necessary columns
           creating dummies and renaming columns.
    """     
    selecting_columns = world_database[["country", "region"]]
    making_dummies = pd.get_dummies(selecting_columns, columns=['region'])
    preprocess_world_data = making_dummies.rename(columns={
        "region_Africa":"africa",
        "region_Asia":"asia",
        "region_Europe":"europe",
        "region_North America":"north_america",
        "region_Oceania":"oceania",
        "region_South America":"south_america"
        })
    return preprocess_world_data
