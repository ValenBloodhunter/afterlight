
from fastapi import FastAPI

app = FastAPI(title="AFTERLIGHT API")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "AFTERLIGHT",
        "message": "Backend is operational"
    }
