from __future__ import annotations
"""Stubbed Databricks client for development."""
import pandas as pd
import os



from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

@dataclass
class DatabricksConfig:
    sql_endpoint: str
    http_path: str
    access_token: str

class DatabricksClient:
    """
    Minimal Databricks client for the walking skeleton.
    For now this can be a stub that returns static data.
    """

    def __init__(self, config: Optional[DatabricksConfig] = None):
        # In the skeleton we can make these optional /  env-based
        self._config = config or DatabricksConfig(
            sql_endpoint=os.getenv("DBX_SQL_ENDPOINT", "dummy"),
            http_path=os.getenv("DBX_HTTP_PATH", "dummy"),
            access_token=os.getenv("DBX_ACCESS_TOKEN", "dummy"),
        )
    
    def query_df(self, sql: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        """
        Execute a SQL query and return results as a pandas DataFrame.
        
        For now, returns hardcoded sample data with columns:
        - tenant_id: str
        - shopper_id: str
        - transaction_ts: datetime
        """
        # TODO: Replace with actual Databricks SQL query
        # Generate sample data
        now = datetime.now(timezone.utc)
        sample_data = {
            'tenant_id': ['demo', 'demo', 'demo', 'demo', 'demo'],
            'shopper_id': ['shopper_1', 'shopper_1', 'shopper_2', 'shopper_3', 'shopper_1'],
            'transaction_ts': [
                now - timedelta(days=5),
                now - timedelta(days=10),
                now - timedelta(days=15),
                now - timedelta(days=20),
                now - timedelta(days=25),
            ]
        }
        return pd.DataFrame(sample_data)

