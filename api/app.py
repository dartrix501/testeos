import json

def handler(request, response):
    try:
        # Obtener datos del POST
        data = request.body
        if not data:
            response.status_code = 400
            response.write(json.dumps({"mensaje": "No se recibieron datos"}))
            return

        # Convertir bytes a JSON
        json_data = json.loads(data.decode("utf-8"))

        nombre = json_data.get("nombre")
        email = json_data.get("email")

        # Lógica Python
        print(f"Nombre: {nombre}, Email: {email}")  # Logs de Vercel

        # Respuesta al frontend
        response.status_code = 200
        response.headers["Content-Type"] = "application/json"
        response.write(json.dumps({"mensaje": f"Datos recibidos: {nombre}, {email}"}))

    except Exception as e:
        response.status_code = 500
        response.write(json.dumps({"mensaje": f"Error interno: {str(e)}"}))
