from typing import Union

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from dotenv import load_dotenv
from api.producto import router_producto
from api.user import router_user
load_dotenv()

app = FastAPI()

app.include_router(router_producto.producto, prefix="/api")
app.include_router(router_user.user, prefix="/user")

# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Rolando@localhost:5432/empresa")

# async def get_db():
#     conn = await asyncpg.connect(DATABASE_URL)
#     try:
#         yield conn
#     finally:
#         await conn.close()



# @app.get("/users")
# async def get_users(db=Depends(get_db)):
#     print(os.getenv("DATABASE_URL_X"))
#     print("DATABASE_URL_______________________________________________")
#     rows = await db.fetch("SELECT numero, asunto FROM documento")
#     users = [{"numero": row["numero"], "asunto": row["asunto"]} for row in rows]
#     return users


