from fastapi import APIRouter, Depends
from config.db import get_db


producto = APIRouter()


# ? CREATE ONE REGISTRO
# ? ****************************************************************************************/
@producto.get("/producto")
def get_Id_User():
    return {"msj": "successfully", "pro": 4555}


@producto.get("/productos")
async def get_users(db=Depends(get_db)):
    # print(os.getenv("DATABASE_URL_X"))
    rows = await db.fetch(' SELECT name, email FROM "User" ')
    users = [{"name": row["name"], "email": row["email"]} for row in rows]
    return users
