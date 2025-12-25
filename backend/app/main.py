from fastapi import FastAPI

app = FastAPI(title="EventRelay")

@app.get("/health")
def health():
    return {"status": "ok"}
