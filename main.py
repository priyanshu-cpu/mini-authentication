from fastapi import FastAPI, HTTPException, Depends
from routers.auth import router as auth_router
from routers.user import router as user_router

app = FastAPI()

app.router(auth_router, tags =["Auth"])
app.router(user_router, tags = ["User"])
