# Vercel Python Serverless
import json

def handler(request, response):
    try:
        data = request.json
        nombre = data.get("nombre")
        email = data.get("email")

        # Aquí ejecutas tu lógica Python
        print(f"Nombre: {nombre}, Email: {email}")  # se ve en los logs de Vercel

        response.status_code = 200
        response.headers["Content-Type"] = "application/json"
        response.write(json.dumps({"mensaje": f"Datos recibidos: {nombre}, {email}"}))

    except Exception as e:
        response.status_code = 500
        response.write(json.dumps({"mensaje": str(e)}))
