```json
{
    "utils/data_preprocessor.py": {
        "content": "
import logging
from typing import List, Dict
from google.cloud import bigquery
from agent_zero import AgentZeroClient
from langfuse import LangGraph

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for the given data.

    Args:
    - data (List[float]): The input data.

    Returns:
    - float: The non-stationary drift index.

    Raises:
    - ValueError: If the input data is empty.
    """
    try:
        if not data:
            raise ValueError('Input data is empty')
        # Calculate the non-stationary drift index using LangGraph
        lang_graph = LangGraph()
        state_graph = lang_graph.StateGraph(data)
        return state_graph.drift_index
    except Exception as e:
        logger.error(f'Error calculating non-stationary drift index: {e}')
        raise

def stochastic_regime_switch(data: List[float]) -> Dict[str, float]:
    """
    Perform stochastic regime switch for the given data.

    Args:
    - data (List[float]): The input data.

    Returns:
    - Dict[str, float]: The regime switch results.

    Raises:
    - ValueError: If the input data is empty.
    """
    try:
        if not data:
            raise ValueError('Input data is empty')
        # Perform stochastic regime switch using AgentZeroClient
        agent_zero_client = AgentZeroClient()
        regime_switch_results = agent_zero_client.regime_switch(data)
        return regime_switch_results
    except Exception as e:
        logger.error(f'Error performing stochastic regime switch: {e}')
        raise

def data_preprocessing(data: List[float]) -> List[float]:
    """
    Preprocess the given data.

    Args:
    - data (List[float]): The input data.

    Returns:
    - List[float]: The preprocessed data.

    Raises:
    - ValueError: If the input data is empty.
    """
    try:
        if not data:
            raise ValueError('Input data is empty')
        # Preprocess the data using BigQuery
        bigquery_client = bigquery.Client()
        preprocessed_data = bigquery_client.query('SELECT * FROM data').to_dataframe()
        return preprocessed_data['value'].tolist()
    except Exception as e:
        logger.error(f'Error preprocessing data: {e}')
        raise

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    non_stationary_drift_index_result = non_stationary_drift_index(data)
    stochastic_regime_switch_result = stochastic_regime_switch(data)
    data_preprocessing_result = data_preprocessing(data)
    logger.info(f'Non-stationary drift index: {non_stationary_drift_index_result}')
    logger.info(f'Stochastic regime switch results: {stochastic_regime_switch_result}')
    logger.info(f'Preprocessed data: {data_preprocessing_result}',
        "
        ,
        "commit_message": "feat: implement specialized data_preprocessor logic"
    }
}
```