from fastapi import APIRouter, Depends
from api.config.db import get_db


producto = APIRouter()



# ? CREATE ONE REGISTRO
# ? ****************************************************************************************/
@producto.get("/user")
def get_Id_User():
    return {"msj": "successfully", "pro": 4555}




@producto.get("/users")
async def get_users(db=Depends(get_db)):
    # print(os.getenv("DATABASE_URL_X"))
    print("DATABASE_URL_______________________________________________")
    rows = await db.fetch("SELECT numero, asunto FROM documento")
    users = [{"numero": row["numero"], "asunto": row["asunto"]} for row in rows]
    return users


