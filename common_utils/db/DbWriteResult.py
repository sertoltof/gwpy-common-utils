from dataclasses import dataclass
from typing import Optional


@dataclass
class DbWriteResult:
    """Essentially a dumber interface to the PyMongo BulkWriteResult class.
    Basic info about how a write operation went"""
    successful: Optional[bool]
    """A None value here indicates the work was not even attempted, probably due to no work being requested."""
    inserted_count: int = 0
    matched_count: int = 0
    modified_count: int = 0
    deleted_count: int = 0
    upserted_count: int = 0
