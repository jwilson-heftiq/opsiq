from __future__ import annotations
"""Retention domain services."""
from datetime import datetime, timedelta, timezone
from typing import List, Optional, Iterable
import pandas as pd

from .models import ShopperTripSummary, RetentionSummary


class RetentionService:
    """
    Pure domain logic: given trip events, compute simple summary stats.
    """
    
    def compute_trip_summaries(
        self,
        trips_df: pd.DataFrame,
        now: datetime | None = None,
        lookback_days: int = 30
    ) -> List[ShopperTripSummary]:
        now = now or datetime.now(timezone.utc)
        cutoff = now - timedelta(days=lookback_days)

        if "transaction_ts" not in trips_df.columns or "shopper_id" not in trips_df.columns:
            # In domain logic you might raise a domain-specific exception
            return []

        # Filter by cutoff
        trips_df = trips_df.copy()
        trips_df["transaction_ts"] = pd.to_datetime(trips_df["transaction_ts"])
        filtered = trips_df[trips_df["transaction_ts"] >= cutoff]

        grouped = filtered.groupby("shopper_id", as_index=False).size()
        grouped.rename(columns={"size": "trip_count_last_30_days"}, inplace=True)

        return [
            ShopperTripSummary(
                shopper_id=row["shopper_id"],
                trip_count_last_30_days=row["trip_count_last_30_days"],
            )
            for _, row in grouped.iterrows()
        ]

        
    
    def compute_retention_summary(
        self,
        summaries: Iterable[ShopperTripSummary]
    ) -> RetentionSummary:
        summaries_list = list(summaries)
        total_shoppers = len(summaries_list)
        total_trips = sum(s.trip_count_last_30_days for s in summaries_list)
        
        return RetentionSummary(
            total_shoppers=total_shoppers,
            total_trips_last_30_days=total_trips
        )

