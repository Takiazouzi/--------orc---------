from fastapi import FastAPI

app = FastAPI(
    title="Smart Document AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status":"running"}
