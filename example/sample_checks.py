from __future__ import annotations

from framework.rules import Rule, ValidationResult
from framework.validators import Validator


def rule_no_null_customer_id() -> ValidationResult:
    failed = 0  # placeholder for demo
    passed = failed == 0

    return ValidationResult(
        rule_name="no_null_customer_id",
        passed=passed,
        message=(
            "customer_id has no nulls"
            if passed
            else f"customer_id has {failed} nulls"
        ),
        failed_count=failed,
    )


def main() -> None:
    rules = [
        Rule(
            name="no_null_customer_id",
            check=rule_no_null_customer_id,
            severity="ERROR",
        )
    ]

    validator = Validator(rules)
    results = validator.run()

    for r in results:
        print(f"[{'PASS' if r.passed else 'FAIL'}] {r.rule_name} - {r.message}")

    validator.fail_if_errors(results)


if __name__ == "__main__":
    main()
