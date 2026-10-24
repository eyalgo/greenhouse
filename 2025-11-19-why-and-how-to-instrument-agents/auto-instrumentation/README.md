# Auto-instrumentation

## Files

- [`main.py`](main.py) — Basic agent loop
- [`tools.py`](tools.py) — File system tools (read, grep, list)
- [`cli.py`](cli.py) — Model selection
- [`utils.py`](utils.py) — Tool execution helpers

## Run

```bash
pip install -r requirements.txt
cp .env.example .env  # Configure environment variables
dotenv run -- opentelemetry-instrument python main.py
```

A wrong port in `OTEL_EXPORTER_OTLP_ENDPOINT` does not stop the agent: it runs as usual and no telemetry reaches your collector. To spot it, set `OTEL_TRACES_EXPORTER=console` in `.env` and run the agent again; if spans print in your terminal, the agent is producing telemetry and the endpoint is what to check. Your collector's logs also show the port it listens on, 4317 by default for OTLP over gRPC.
