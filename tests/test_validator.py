import pytest

from framework.rules import Rule, ValidationResult
from framework.validators import Validator


def test_validator_passes_when_all_rules_pass() -> None:
    def ok() -> ValidationResult:
        return ValidationResult("ok", True, "all good", 0)

    v = Validator([Rule("ok", ok)])
    results = v.run()
    assert results[0].passed is True


def test_validator_fails_when_rule_fails() -> None:
    def bad() -> ValidationResult:
        return ValidationResult("bad", False, "failed", 1)

    v = Validator([Rule("bad", bad)])

    with pytest.raises(AssertionError):
        v.fail_if_errors(v.run())
