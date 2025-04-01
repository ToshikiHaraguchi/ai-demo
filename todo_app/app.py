from fastapi import FastAPI
from routes.task_routes import router

app = FastAPI()

# ルーティングを追加
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API"}