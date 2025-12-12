from __future__ import annotations

from datetime import datetime, timedelta, timezone

from engines.retention.domain.services import RetentionService
from engines.retention.ports.inbound import RetentionQueryPort, RetentionSummaryDTO
from engines.retention.ports.outbound import ShopperEventsPort
from platform_core.ports.tenant_ports import TenantResolverPort


class RetentionQueryService(RetentionQueryPort):
    """Service that implements RetentionQueryPort."""

    def __init__(
        self,
        tenant_resolver: TenantResolverPort,
        shopper_events_port: ShopperEventsPort,
        retention_service: RetentionService | None = None,
    ) -> None:
        """Initialize with required dependencies."""
        self._tenant_resolver = tenant_resolver
        self._shopper_events_port = shopper_events_port
        self._retention_service = retention_service or RetentionService()

    def get_summary(self, tenant_id: str) -> RetentionSummaryDTO:
        # Resolve tenant
        tenant = self._tenant_resolver.get_tenant(tenant_id)

        # Load trips from last 30 days
        now = datetime.now(timezone.utc)
        since = now - timedelta(days=30)

        trips_df = self._shopper_events_port.load_trips(tenant, since)

        # Compute summaries
        summaries = self._retention_service.compute_trip_summaries(
            trips_df,
            now=now
        )
        summary = self._retention_service.compute_retention_summary(summaries)

        return RetentionSummaryDTO(
            total_shoppers=summary.total_shoppers,
            total_trips_last_30_days=summary.total_trips_last_30_days,
        )

