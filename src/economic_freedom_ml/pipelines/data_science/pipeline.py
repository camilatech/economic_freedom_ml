"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from economic_freedom_ml.pipelines.data_science.nodes import fit_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node (
                func=fit_model,
                inputs=['data_for_prophet'],
                outputs='mercosur_predictions',
                name='mercosur_predictions_node'
            ),
    ])