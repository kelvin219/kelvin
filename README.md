# Kelvin POD Layer Services

This repository contains skeleton implementations for the POD layer microservices
of the Kelvin HFT platform. Each service is independent with its own build
instructions and Dockerfile.

## Services
- `pod-market-data-ingest` – C++ service to parse market data via DPDK.
- `pod-orderbook-svc` – Rust order book with ChronicleMap backend.
- `pod-bus` – Rust lock-free event bus with ns timestamps.
- `pod-fpga-bridge` – Rust interface to FPGA using UIO/mmap.
- `pod-strategy-svc` – Rust micro-book market making strategies.
- `pod-risk-gate` – Go service implementing eBPF kill switch.
- `pod-smart-order-router` – Rust router to multiple venues.
- `pod-oms-local` – Rust service logging orders with SBE.

Each directory contains a `README.md` with build, run, and test instructions.
