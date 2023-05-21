"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from economic_freedom_ml.pipelines.data_processing.nodes import preprocess_raw_data, preprocess_world

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node (
                func=preprocess_raw_data,
                inputs=['heritage_foundation_database'],
                outputs='preprocess_data',
                name='preprocess_raw_data_node'
            ),
            node (
                func=preprocess_world,
                inputs=['world_database'],
                outputs='preprocess_world_data',
                name='preprocess_world_data_node'
            ),            
    ])
