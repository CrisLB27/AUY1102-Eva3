from flask import Flask, render_template_string

app = Flask(__name__)


inventory = [
    {"id": 1, "name": "Servidor Dell PowerEdge", "status": "active", "location": "Rack A"},
    {"id": 2, "name": "Switch Cisco Catalyst", "status": "maintenance", "location": "Rack B"},
    {"id": 3, "name": "Firewall Fortinet", "status": "active", "location": "Perímetro"},
    {"id": 4, "name": "NAS Synology", "status": "active", "location": "Respaldo"}
]

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Inventario Simple</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        h1 { color: #333; text-align: center; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); border-radius: 8px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px; border: 1px solid #ddd; text-align: left; }
        th { background-color: #007bff; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        .status-active { color: green; font-weight: bold; }
        .status-maintenance { color: orange; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Inventario de Equipos TI</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Dispositivo</th>
                    <th>Ubicación</th>
                    <th>Estado</th>
                </tr>
            </thead>
            <tbody>
                {% for item in inventory %}
                <tr>
                    <td>{{ item.id }}</td>
                    <td>{{ item.name }}</td>
                    <td>{{ item.location }}</td>
                    <td class="status-{{ item.status }}">{{ item.status|upper }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # Renderizamos la variable HTML_PAGE pasando los datos del inventario
    return render_template_string(HTML_PAGE, inventory=inventory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
