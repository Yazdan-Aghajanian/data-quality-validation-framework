# Overview

This repository provides a lightweight, CI-ready data quality validation framework
designed for lakehouse and data engineering pipelines.

## Purpose

The framework enables:

- Rule-based validation checks
- Structured validation results
- Fail-fast behaviour for CI/CD pipelines
- Extensible rule definitions
- Clear separation between validation logic and execution

## Target Use Cases

- Bronze → Silver → Gold validation gates
- Delta Lake quality checks
- Pre-merge CI validation
- Production data contract enforcement
- Automated data observability patterns

## Architecture

- `framework/` → Core validation engine
- `example/` → Demonstration usage
- `tests/` → Unit tests
- `.github/workflows/` → CI automation
