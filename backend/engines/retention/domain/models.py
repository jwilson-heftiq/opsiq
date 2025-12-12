from __future__ import annotations

"""Retention domain models."""
from dataclasses import dataclass


@dataclass
class ShopperTripSummary:
    """Summary of trips for a single shopper."""
    shopper_id: str
    trip_count_last_30_days: int


@dataclass
class RetentionSummary:
    """Retention summary for a tenant."""
    total_shoppers: int
    total_trips_last_30_days: int

