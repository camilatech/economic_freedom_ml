"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from economic_freedom_ml.pipelines import data_processing as dp
from economic_freedom_ml.pipelines import feature_engineering as fe
from economic_freedom_ml.pipelines import data_science as ds

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline = dp.create_pipeline()
    feature_engineering_pipeline = fe.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    return {
        "dp": data_processing_pipeline,
        "fe": feature_engineering_pipeline,
        "ds": data_science_pipeline,
        "__default__": data_processing_pipeline+feature_engineering_pipeline+data_science_pipeline
    }