from fastapi import FastAPI, HTTPException, Depends
from routers.auth import router as auth_router
from routers.user import router as user_router

app = FastAPI()

app.include_router(auth_router, tags =["Auth"])
app.include_router(user_router, tags = ["User"])
