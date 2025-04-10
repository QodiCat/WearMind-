from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="AI CyberWardrobe API",
    description="Backend API for AI-powered wardrobe management system",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Welcome to AI CyberWardrobe API"}

# Import and include routers
# from app.api import users, wardrobe, recommendations, etc.
# app.include_router(users.router, prefix="/api/users", tags=["users"])
# app.include_router(wardrobe.router, prefix="/api/wardrobe", tags=["wardrobe"])
# app.include_router(recommendations.router, prefix="/api/recommendations", tags=["recommendations"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 