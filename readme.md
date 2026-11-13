# GitHub Actions — Python Testing Exercise

This repo is a hands-on exercise for learning how automated testing and GitHub Actions work together.

## Getting Started

Read [`exercise.md`](exercise.md) — it walks you through every step from forking the repo to seeing your tests go green in the cloud.

## What's in this repo

| File | Description |
|------|-------------|
| `calc.py` | A calculator with a `calculate()` function (incomplete — you will fix it) |
| `greet.py` | A greeting script with a `greet_user()` function (incomplete — you will fix it) |
| `test_calc.py` | pytest tests for the calculator |
| `test_greet.py` | pytest tests for the greeting function |
| `requirements.txt` | Python dependencies (`pytest`) |
| `.github/workflows/test.yml` | CI pipeline — runs all tests on every push |
