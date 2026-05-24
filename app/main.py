from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total Request Count"
)

@app.get("/")
def root():
    REQUEST_COUNT.inc()

    return {
        "status": "running",
        "platform": "kubernetes"
    }

@app.get("/health")
def health():
    return {"health": "ok"}

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )