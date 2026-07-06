import os
import uuid
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.core.celery_app import celery_app
from app.core.config import settings

app = FastAPI(title="Smart Document AI - API Gateway")

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Smart Document AI API Gateway is running"}

@app.post("/api/v1/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    file_id = str(uuid.uuid4())
    ext = file.filename.split(".")[-1] if "." in file.filename else "jpg"
    file_path = f"{settings.UPLOAD_DIR}/{file_id}.{ext}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    task = celery_app.send_task(
        "process_ocr",
        args=[file_path, file_id],
        queue="ocr_queue"
    )

    return JSONResponse(
        status_code=202,
        content={
            "message": "Document queued for processing",
            "task_id": task.id,
            "file_id": file_id
        }
    )

@app.get("/api/v1/documents/status/{task_id}")
def get_task_status(task_id: str):
    task = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task.status,
        "result": str(task.result) if task.status == "SUCCESS" else None
    }
