"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.4
"""
import pandas as pd 

def preprocess_raw_data (heritage_foundation_database: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for election_data.

    Args:
        election_data: Raw data.
    Returns:
        Preprocessed data with:
           blanck and null votes columns deleted, 
           also the roll "Territory Nacional" as it is a agreggation of all other rows.
    """      
    heritage_foundation_database.rename(columns={
        "Name": "name",
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
    return heritage_foundation_database



