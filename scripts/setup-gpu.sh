#!/usr/bin/env bash
set -euo pipefail

echo "[gpu-setup] Checking NVIDIA runtime availability..."
if command -v nvidia-smi >/dev/null 2>&1; then
  nvidia-smi
else
  echo "[gpu-setup] nvidia-smi not found on host."
fi

echo "[gpu-setup] Checking Docker GPU support..."
if docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi; then
  echo "[gpu-setup] Docker GPU runtime is available."
else
  echo "[gpu-setup] Docker GPU runtime is unavailable. Install NVIDIA Container Toolkit."
  exit 1
fi
