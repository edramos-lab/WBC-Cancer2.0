from fastapi import FastAPI

app = FastAPI()

@app.get("/models")
async def get_available_models():
    return {"available_models": ["model1", "model2"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
