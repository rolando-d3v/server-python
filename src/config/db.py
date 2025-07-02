import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()



# Obtener el valor de una variable de entorno.
port_server = os.getenv("DATABASE_URL")


print(f"{port_server}")


DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Rolando@localhost:5432/universidad")

# obtener la conexión a la base de datos
async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()




# verificar que la base de datos esté corriendo
async def verificar_base_datos():
    """Verifica que la base de datos esté corriendo"""
    try:
        async for conn in get_db():
            print("✅ Base de datos conectada y funcionando correctamente")
            await conn.close()
            break
    except Exception as e:
        print(f"❌ Error conectando a la base de datos: {e}")
