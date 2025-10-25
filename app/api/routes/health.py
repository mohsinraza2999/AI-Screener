from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
def health_check():
    """
    Basic health check endpoint.
    Returns service status and current timestamp.
    Useful for monitoring, Docker/K8s probes, and CI/CD checks.
    """
    return {
        "status": "ok",
        "service": "ai_screener",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
