from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "success", "message": "CI/CD works!"}
