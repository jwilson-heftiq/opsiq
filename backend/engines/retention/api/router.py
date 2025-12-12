from __future__ import annotations

from fastapi import APIRouter, HTTPException

from engines.retention.adapters.dbx_shopper_events_adapter import DatabricksShopperEventsAdapter
from engines.retention.adapters.retention_query_service import RetentionQueryService
from engines.retention.ports.inbound import RetentionSummaryDTO
from platform_core.adapters.inmemory_tenant_resolver import InMemoryTenantResolver
from shared.infra.dbx_client import DatabricksClient

# Initialize dependencies
_tenant_resolver = InMemoryTenantResolver()
_dbx_client = DatabricksClient()
_shopper_events_adapter = DatabricksShopperEventsAdapter(_dbx_client)
_retention_query_service = RetentionQueryService(
    tenant_resolver=_tenant_resolver,
    shopper_events_port=_shopper_events_adapter,
)

router = APIRouter()


@router.get("/{tenant_id}/retention/summary", response_model=RetentionSummaryDTO)
def get_retention_summary(tenant_id: str):
    """
    Get retention summary for a tenant.

    Args:
        tenant_id: The tenant ID

    Returns:
        RetentionSummaryDTO with retention metrics
    """
    try:
        return _retention_query_service.get_summary(tenant_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

