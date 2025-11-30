from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Containerized Quote API"}

@app.get("/api/quote")
def get_quote():
    # This is a static quote for now, demonstrating API functionality.
    return {"quote": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela"}