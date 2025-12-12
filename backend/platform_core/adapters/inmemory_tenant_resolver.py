from __future__ import annotations

"""In-memory tenant resolver implementation."""

from platform_core.domain.tenants import Tenant
from platform_core.ports.tenant_ports import TenantResolverPort


class InMemoryTenantResolver(TenantResolverPort):
    """In-memory implementation of TenantResolverPort."""

    def __init__(self, tenants: dict[str, Tenant] | None = None) -> None:
        """Initialize with a default tenant."""
        self._tenants = tenants or {
            'demo': Tenant(
                id='demo',
                name='Demo Tenant',
                catalog='demo_catalog',
                schema='demo_schema'
            ),
        }

    def get_tenant(self, tenant_id: str) -> Tenant:
        try:
            return self._tenants[tenant_id]
        except KeyError:
            # In production you'd raise a domain-specific error
            raise ValueError(f"Unknown tenant_id={tenant_id!r}")

