from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

import pandas as pd

from platform_core.domain.tenants import Tenant
from engines.retention.ports.outbound import ShopperEventsPort
from shared.infra.dbx_client import DatabricksClient


class DatabricksShopperEventsAdapter(ShopperEventsPort):
    """Adapter that uses DatabricksClient to load shopper trip events."""
    
    def __init__(self, client: DatabricksClient) -> None:
        """Initialize with a DatabricksClient."""
        self._client = client
    
    def load_trips(self, tenant: Tenant, since: datetime) -> pd.DataFrame:
        # For the skeleton, we ignore catalog/schema, but they're available on tenant.
        """
        Load trip data for a tenant since a given datetime.
        
        Args:
            tenant: The tenant to load trips for
            since: Load trips since this datetime
        
        Returns:
            DataFrame with columns: tenant_id, shopper_id, transaction_ts
        """
        # For now, we'll query all data and filter by tenant and date
        # In a real implementation, this would be a proper SQL query with parameters
        sql = """
        SELECT tenant_id, shopper_id, transaction_ts
        FROM demo.transactions
        WHERE tenant_id = :tenant_id
        AND transaction_ts >= :since
        """
        params: Dict[str, Any] = {
            'tenant_id': tenant.id,
            'since': since.isoformat(),
        }

        
        return self._client.query_df(sql, params)

