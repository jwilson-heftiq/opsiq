from __future__ import annotations

"""Outbound ports for retention engine."""
from abc import ABC, abstractmethod
from datetime import datetime

import pandas as pd

from platform_core.domain.tenants import Tenant


class ShopperEventsPort(ABC):
    """Port for loading shopper trip events."""

    @abstractmethod
    def load_trips(self, tenant: Tenant, since: datetime) -> pd.DataFrame:
        """Load trip-level events for a tenant since a given cutoff date."""
        raise NotImplementedError

