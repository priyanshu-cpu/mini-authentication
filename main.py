from fastapi import FastAPI, HTTPException, Depends


app = FastAPI()

app.include_router()