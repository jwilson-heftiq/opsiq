from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class RetentionSummaryDTO:
    """Data transfer object for retention summary."""
    total_shoppers: int
    total_trips_last_30_days: int


class RetentionQueryPort(ABC):
    """Port for querying retention summaries."""

    @abstractmethod
    def get_summary(self, tenant_id: str) -> RetentionSummaryDTO:
        """
        Return a minimal retention summary for a tenant.
        """
        raise NotImplementedError

