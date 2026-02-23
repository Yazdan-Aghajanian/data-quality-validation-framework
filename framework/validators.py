from __future__ import annotations

from typing import Iterable, List

from framework.rules import Rule, ValidationResult


class Validator:
    def __init__(self, rules: Iterable[Rule]):
        self.rules = list(rules)

    def run(self) -> List[ValidationResult]:
        results: List[ValidationResult] = []
        for rule in self.rules:
            results.append(rule.check())
        return results

    @staticmethod
    def fail_if_errors(results: List[ValidationResult]) -> None:
        errors = [r for r in results if (not r.passed and r.failed_count >= 0)]
        if any(not r.passed for r in errors):
            raise AssertionError("Data quality validation failed (one or more rules did not pass).")
