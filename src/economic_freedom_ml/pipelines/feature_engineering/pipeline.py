"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from economic_freedom_ml.pipelines.feature_engineering.nodes import creating_features

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node (
                func=creating_features,
                inputs=['preprocess_data', 'preprocess_world_data'],
                outputs='data_with_features',
                name='data_with_features_node'
            ),          
    ])
