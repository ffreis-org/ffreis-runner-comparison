"""Optional ghz wrapper (gRPC load)."""

from __future__ import annotations

from subprocess import call as subprocess_call


def run_ghz(target: str, proto_path: str, duration_s: int = 30) -> int:
    cmd = [
        "ghz",
        "--insecure",
        "--proto",
        proto_path,
        "--call",
        "onnxserving.grpc.InferenceService.Live",
        "--duration",
        f"{duration_s}s",
        target,
    ]
    return subprocess_call(cmd)
