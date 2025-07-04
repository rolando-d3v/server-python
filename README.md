# Fastapi - asyncpg


source venv/Scripts/activate //entrar y activar virtual en gitbash


deactivate //salir de entorno virtual

python -m venv venv

pip install "fastapi[standard]"



fastapi dev main.py
fastapi dev src/main.py






Como Cursor está basado en VS Code, puedes usar la misma configuración.

📍 Pasos:
Abre la paleta de comandos con Ctrl + Shift + P.

Escribe Preferences: Open Settings (JSON) y selecciona esa opción.

Agrega:


"files.exclude": {
  "**/__pycache__": true
}



- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
