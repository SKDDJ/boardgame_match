import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
import uvicorn

from fastapi import FastAPI
from app.api.routers import users, events, reviews, matchmaking

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
app.include_router(matchmaking.router, prefix="/matchmaking", tags=["matchmaking"])


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
