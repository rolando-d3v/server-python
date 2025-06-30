from typing import Union

from fastapi import FastAPI, Depends
from pydantic import BaseModel
import asyncpg
import os
from dotenv import load_dotenv
# from src.routes.user_router import router as user_router
from api.producto import producto
load_dotenv()

app = FastAPI()

# app.include_router(user_router)

# app.include_router(producto_router.producto)
app.include_router(producto.producto, prefix="/api")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Rolando@localhost:5432/empresa")

async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()



# @app.get("/users")
# async def get_users(db=Depends(get_db)):
#     print(os.getenv("DATABASE_URL_X"))
#     print("DATABASE_URL_______________________________________________")
#     rows = await db.fetch("SELECT numero, asunto FROM documento")
#     users = [{"numero": row["numero"], "asunto": row["asunto"]} for row in rows]
#     return users


