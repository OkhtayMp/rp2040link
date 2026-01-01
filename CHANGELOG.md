# Changelog

## 0.1.3 - 2026-01-01
- Hardened Trusted Publishing workflows for okhtaymp/rp2040link (least-privilege OIDC, twine check, pip cache, workflow_dispatch).
- Added optional TestPyPI workflow for rc tags (v*rc*).
- Added non-context-manager usage improvements (auto_open, lazy_open, connect/disconnect, is_open).

## 0.1.2 - 2026-01-01
- Added connect()/disconnect() aliases, is_open property.
- Added auto_open/lazy_open options and atexit close registration.
- Updated pyproject license metadata to avoid upcoming setuptools deprecations.

## 0.1.1 - 2025-12-31
- Added PyPI publishing workflow (Trusted Publishing via GitHub OIDC).
- Made project metadata PyPI-ready (URL placeholders, publishing docs).

## 0.1.0 - 2025-12-31
- Initial public scaffold: polarity-aware GPIO, binary helpers, PWM, Servo, NeoPixel, I2C/SPI sync wrappers, CLI.
