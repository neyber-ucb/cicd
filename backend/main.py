from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ToDo List API",
    description="A simple ToDo list application with JWT authentication",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the ToDo List API!",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/api/health")
async def health_check():
    """Health check endpoint that validates database connection"""
    from app.database import check_db_connection

    db_healthy = check_db_connection()

    if not db_healthy:
        return {"status": "unhealthy", "database": "disconnected"}

    return {"status": "healthy", "database": "connected"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
