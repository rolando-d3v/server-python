from fastapi import APIRouter, Depends, HTTPException, status
from config.db import get_db
from uuid import uuid4

producto = APIRouter()

#? CREATE ONE REGISTRO
#? ****************************************************************************************/
@producto.get("/get-one/{id}")
def get_Id_User(id: int):
    uuid = uuid4()
    return {"msj": "successfully rolando", "pro": id, "uuid": uuid}





#? OBTENER  PRODUCTOS
#? ****************************************************************************************/
@producto.get("/get-all")
async def get_users(db=Depends(get_db)):
    rows = await db.fetch(' SELECT name, apellido FROM "user" ')

    # si no existe los usuarios
    if not rows:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se encontraron usuarios"
        )
        
    users = [{"name": row["name"], "apellido": row["apellido"]} for row in rows]
    return users
