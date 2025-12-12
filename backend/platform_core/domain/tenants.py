from __future__ import annotations
"""Tenant domain model."""


from dataclasses import dataclass


@dataclass
class Tenant:
    """Represents a tenant in the system."""
    id: str
    name: str
    catalog: str | None = None
    schema: str | None = None

