from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "smartdoc_gateway",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_routes={
        "process_ocr": {"queue": "ocr_queue"},
        "process_nlp": {"queue": "nlp_queue"},
    }
)
