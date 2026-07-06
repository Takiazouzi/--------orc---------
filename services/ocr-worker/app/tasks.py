from app.core.celery_app import celery_app

@celery_app.task(name="process_ocr")
def process_ocr(file_path: str, file_id: str):
    print(f"[OCR Worker] Starting OCR for file: {file_path} (ID: {file_id})")
    
    # TODO: Integrate your existing pipeline here in the next step
    # from app.pipeline.pipeline import run_pipeline
    # extracted_text = run_pipeline(file_path)
    
    extracted_text = "Mock text from OCR"
    
    # Pass the extracted text to the NLP worker
    celery_app.send_task(
        "process_nlp",
        args=[extracted_text, file_id],
        queue="nlp_queue"
    )
    
    return {"status": "OCR completed", "file_id": file_id}
