```json
{
    "utils/data_loader.py": {
        "content": "
import logging
from typing import List, Dict
from google.cloud import bigquery
from agent_zero import AgentZeroClient
from langfuse import LangGraph

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_non_stationary_drift_index(data: List[Dict]) -> List[float]:
    """
    Load non-stationary drift index from data.

    Args:
    - data (List[Dict]): List of dictionaries containing data.

    Returns:
    - List[float]: List of non-stationary drift indices.

    Raises:
    - Exception: If data is invalid.
    """
    try:
        # Initialize LangGraph client
        lang_graph = LangGraph()
        # Initialize AgentZero client
        agent_zero = AgentZeroClient()
        # Load data into BigQuery
        bigquery_client = bigquery.Client()
        table_id = 'autonomous_knitwear_design_optimization_engine.data'
        bigquery_client.load_table_from_json(data, table_id)
        # Load non-stationary drift index using LangGraph
        non_stationary_drift_index = lang_graph.load_non_stationary_drift_index(data)
        # Apply stochastic regime switch using AgentZero
        stochastic_regime_switch = agent_zero.apply_stochastic_regime_switch(non_stationary_drift_index)
        return stochastic_regime_switch
    except Exception as e:
        logger.error(f'Error loading non-stationary drift index: {e}')
        raise

def load_stochastic_regime_switch(data: List[Dict]) -> List[float]:
    """
    Load stochastic regime switch from data.

    Args:
    - data (List[Dict]): List of dictionaries containing data.

    Returns:
    - List[float]: List of stochastic regime switches.

    Raises:
    - Exception: If data is invalid.
    """
    try:
        # Initialize LangGraph client
        lang_graph = LangGraph()
        # Initialize AgentZero client
        agent_zero = AgentZeroClient()
        # Load data into BigQuery
        bigquery_client = bigquery.Client()
        table_id = 'autonomous_knitwear_design_optimization_engine.data'
        bigquery_client.load_table_from_json(data, table_id)
        # Load stochastic regime switch using LangGraph
        stochastic_regime_switch = lang_graph.load_stochastic_regime_switch(data)
        # Apply non-stationary drift index using AgentZero
        non_stationary_drift_index = agent_zero.apply_non_stationary_drift_index(stochastic_regime_switch)
        return non_stationary_drift_index
    except Exception as e:
        logger.error(f'Error loading stochastic regime switch: {e}')
        raise

if __name__ == '__main__':
    # Simulate 'Rocket Science' problem
    data = [
        {'id': 1, 'value': 10.0},
        {'id': 2, 'value': 20.0},
        {'id': 3, 'value': 30.0}
    ]
    non_stationary_drift_index = load_non_stationary_drift_index(data)
    stochastic_regime_switch = load_stochastic_regime_switch(data)
    logger.info(f'Non-stationary drift index: {non_stationary_drift_index}')
    logger.info(f'Stochastic regime switch: {stochastic_regime_switch}'
        ,
        "commit_message": "feat: implement specialized data_loader logic"
    }
}
```