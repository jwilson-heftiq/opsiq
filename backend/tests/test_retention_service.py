from datetime import datetime, timedelta, timezone

import pandas as pd

from engines.retention.domain.services import RetentionService


def test_compute_trip_summaries_counts_correctly():
    now = datetime.now(timezone.utc)
    trips_df = pd.DataFrame(
        [
            {"shopper_id": "s1", "transaction_ts": now - timedelta(days=1)},
            {"shopper_id": "s1", "transaction_ts": now - timedelta(days=5)},
            {"shopper_id": "s2", "transaction_ts": now - timedelta(days=2)},
            # Out of lookback window
            {"shopper_id": "s3", "transaction_ts": now - timedelta(days=40)},
        ]
    )

    service = RetentionService()
    summaries = service.compute_trip_summaries(trips_df, now=now)

    assert len(summaries) == 2  # s1 and s2
    s1 = next(s for s in summaries if s.shopper_id == 's1')
    assert s1.trip_count_last_30_days == 2


def test_compute_retention_summary_aggregates_totals():
    service = RetentionService()
    summaries = [
        service.compute_trip_summaries(
            pd.DataFrame(
                [
                    {"shopper_id": "s1", "transaction_ts": datetime.now(timezone.utc)},
                    {"shopper_id": "s2", "transaction_ts": datetime.now(timezone.utc)},
                ]
            )
        )
    ]
    # flatten list of lists
    summaries_flat = [item for sublist in summaries for item in sublist]
    summary = service.compute_retention_summary(summaries_flat)
    assert summary.total_shoppers == 2
    assert summary.total_trips_last_30_days == 2