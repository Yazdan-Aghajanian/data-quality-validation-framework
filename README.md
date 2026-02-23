# Data Quality Validation Framework

CI-ready data quality validation framework for lakehouse pipelines.

## What it includes
- Rule-based checks (nulls, duplicates, thresholds, schema)
- Structured results (pass/fail, failed counts, messages)
- Unit tests + GitHub Actions CI

## Quick start
```bash
pip install -r requirements-dev.txt
python example/sample_checks.py
pytest -q
