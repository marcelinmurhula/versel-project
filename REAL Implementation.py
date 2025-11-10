from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="VERSEL API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/media", StaticFiles(directory="../media"), name="media")

@app.post("/api/generate")
async def generate_video():
    return {
        "success": True,
        "message": "VERSEL is working!",
        "stepwiseLogic": {
            "domain": "Physics",
            "steps": ["Step 1", "Step 2", "Step 3"],
            "animationEngine": "manim"
        }
    }

@app.get("/")
async def root():
    return {"message": "VERSEL API Running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
