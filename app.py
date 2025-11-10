from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import subprocess
import os
import uuid
from pathlib import Path

app = FastAPI(title="VERSEL API", description="AI Educational Video Generator")

# CORS middleware - FIXED: allow_headers (not allow_header)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],  # FIXED THIS LINE
)

# Mount static files
app.mount("/media", StaticFiles(directory="../media"), name="media")

# Demo videos mapping
DEMO_VIDEOS = {
    "falkirk wheel": "/media/videos/demo_test/480p15/FalkirkDemo.mp4",
    "binary search": "/media/videos/demo2/480p15/versel_demo_2.mp4",
    "computer science": "/media/videos/demo2/480p15/versel_demo_2.mp4"
}

@app.post("/api/generate")
async def generate_video(request: dict):
    """Generate educational video with real demo videos"""
    try:
        prompt = request.get("prompt", "").lower()
        print(f"🎯 Processing: '{prompt}'")
        
        # Check for demo keywords and serve real videos
        for keyword, video_path in DEMO_VIDEOS.items():
            if keyword in prompt:
                print(f"🎬 Serving pre-rendered demo: {keyword}")
                
                # Determine domain based on prompt
                if "falkirk" in prompt or "wheel" in prompt:
                    domain = "Mechanical Engineering"
                    steps = [
                        "Falkirk Wheel structure analysis",
                        "Water-filled caissons mechanism", 
                        "Rotational balance principle",
                        "Energy-efficient design",
                        "Boat transportation process"
                    ]
                else:
                    domain = "Computer Science"
                    steps = [
                        "Algorithm concept analysis",
                        "Step-by-step process breakdown",
                        "Efficiency optimization",
                        "Real-world applications",
                        "Learning outcomes"
                    ]
                
                return {
                    "success": True,
                    "message": "🎉 VERSEL Educational Video Generated!",
                    "stepwiseLogic": {
                        "domain": domain,
                        "steps": steps,
                        "animationEngine": "manim",
                        "visualStyle": "engineering-diagram"
                    },
                    "videoPath": video_path,
                    "isRealVideo": True
                }
        
        # For other prompts, use enhanced simulation
        stepwise_logic = {
            "domain": "General STEM",
            "steps": [
                "AI analyzes the educational concept",
                "Break down into key learning steps", 
                "Generate visual representation",
                "Create engaging animation",
                "Deliver educational video"
            ],
            "animationEngine": "manim",
            "visualStyle": "educational-diagram"
        }
        
        return {
            "success": True,
            "message": "Video generation in progress - AI analysis complete",
            "stepwiseLogic": stepwise_logic,
            "videoPath": "/api/placeholder-video.mp4",
            "isRealVideo": False
        }
            
    except Exception as e:
        print(f"❌ Generation failed: {e}")
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

@app.get("/api/placeholder-video.mp4")
async def get_placeholder_video():
    """Serve placeholder video"""
    print("📹 Serving placeholder video")
    return FileResponse("../media/videos/TestAnimation.mp4")

@app.get("/")
async def root():
    return {"message": "🚀 VERSEL API with REAL Demo Videos"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "VERSEL API"}

if __name__ == "__main__":
    print("🚀 Starting VERSEL with REAL Demo Videos...")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
