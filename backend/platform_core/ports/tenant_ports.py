from __future__ import annotations

from abc import ABC, abstractmethod
from . import __init__ # noqa: F401 
from platform_core.domain.tenants import Tenant


class TenantResolverPort(ABC):
    """Port for resolving tenants by ID."""
    
    @abstractmethod
    def get_tenant(self, tenant_id: str) -> Tenant:
        """Return tenant configuration or raise if not found."""
        raise NotImplementedError

