from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass(frozen=True)
class ValidationResult:
    rule_name: str
    passed: bool
    message: str
    failed_count: int = 0


@dataclass(frozen=True)
class Rule:
    name: str
    check: Callable[[], ValidationResult]
    severity: str = "ERROR"  # ERROR | WARN
    owner: Optional[str] = None
