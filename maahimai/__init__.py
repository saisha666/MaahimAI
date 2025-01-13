# Disable OpenTelemetry SDK
import os
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["EC_TELEMETRY"] = "false"
from .cli import MaahimAI
from .version import __version__ = "2.0.18"