from fastapi import APIRouter, Depends
from config.db import get_db


user = APIRouter()


# ? CREATE ONE REGISTRO
# ? ****************************************************************************************/
@user.get("/get-user")
def get_Id_User():
    return {"msj": "successfully usuario", "pro": 4555}
