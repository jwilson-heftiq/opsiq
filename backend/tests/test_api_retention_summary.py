from fastapi.testclient import TestClient
from main import app

def test_retention_summary_endpoint_returns_valid_response(monkeypatch):
    # monkeypatch Databricks client to avoid real calls
    from engines.retention.api.router import _dbx_client
    from datetime import datetime, timedelta, timezone

    def mock_query_df(sql, params=None):
        import pandas as pd
        now = datetime.now(timezone.utc)
        return pd.DataFrame(
            [
                {"tenant_id": "demo", "shopper_id": "s1", "transaction_ts": now - timedelta(days=5)},
                {"tenant_id": "demo", "shopper_id": "s2", "transaction_ts": now - timedelta(days=10)},
            ]
        )
    monkeypatch.setattr(_dbx_client, "query_df", mock_query_df)

    client = TestClient(app)
    res = client.get("tenants/demo/retention/summary")
    assert res.status_code == 200
    data = res.json()
    assert data["total_shoppers"] == 2
    assert data["total_trips_last_30_days"] == 2