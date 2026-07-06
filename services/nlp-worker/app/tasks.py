from app.core.celery_app import celery_app

@celery_app.task(name="process_nlp")
def process_nlp(extracted_text: str, file_id: str):
    print(f"[NLP Worker] Received text for file {file_id}: '{extracted_text}'")
    
    # TODO: In the next step, we will add Language Detection, Embeddings, and DB saving here
    # from app.nlp.stages.language import detect_language
    # from app.nlp.stages.embeddings import generate_embeddings
    # from app.db.repository import save_document
    
    print(f"[NLP Worker] Successfully processed and saved document {file_id}!")
    
    return {"status": "NLP completed", "file_id": file_id}
