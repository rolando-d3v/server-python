from fastapi import FastAPI
from dotenv import load_dotenv
import os

from api.producto import router_producto
from api.user import router_user
from config.db import verificar_base_datos
load_dotenv()


app = FastAPI()

# obtener el puerto desde el archivo .env
port_server = int(os.getenv("PORT"))


# evento que se ejecuta al iniciar la aplicación
@app.on_event("startup")
async def startup_event():
    """Evento que se ejecuta al iniciar la aplicación"""
    print(f"🚀 Iniciando servidor FastAPI... in port {port_server}")
    await verificar_base_datos()
    print("🎉 Servidor listo para recibir peticiones!")


# routers
app.include_router(router_producto.producto, prefix="/producto")
app.include_router(router_user.user, prefix="/user")















# ejemplo de auth middleware

# from fastapi import Request, HTTPException, status, Depends


# # Simulación de tokens válidos
# fake_users = {
#     "admin-token": {"username": "admin", "role": "admin"},
#     "user-token": {"username": "maria", "role": "user"},
# }


# async def auth(request: Request):
#     auth_header = request.headers.get("Authorization")

#     if not auth_header:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Token requerido")

#     token = auth_header.replace("Bearer ", "")
#     user = fake_users.get(token)

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

#     # Guardamos el usuario en el request
#     request.state.user = user

#     # ---------------------------------------



# from fastapi import APIRouter, Request, Depends

# router = APIRouter()


# @router.post("/upload")
# async def crear_archivo(request: Request, _: dict = Depends(auth)):
#     user = request.state.user
#     return {
#         "message": "Archivo subido correctamente",
#         "by": user["username"],
#         "role": user["role"]
#     }
