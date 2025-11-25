from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)


inventory = [
    {"id": 1, "name": "Servidor Dell PowerEdge", "status": "active", "location": "Rack A"},
    {"id": 2, "name": "Switch Cisco Catalyst", "status": "maintenance", "location": "Rack B"},
    {"id": 3, "name": "Firewall Fortinet", "status": "active", "location": "Perímetro"}
]



TEMA_BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Sistema IT</title>
    <style>
        body { font-family: sans-serif; margin: 0; background: #f0f2f5; }
        nav { background: #2c3e50; padding: 15px; }
        nav a { color: white; text-decoration: none; margin-right: 20px; font-weight: bold; }
        nav a:hover { text-decoration: underline; }
        .container { background: white; max-width: 800px; margin: 30px auto; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h1 { color: #333; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        
        /* Tablas */
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
        th { background: #3498db; color: white; }
        
        /* Formulario */
        input, select { width: 100%; padding: 8px; margin: 5px 0 15px 0; display: block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;}
        button { background: #27ae60; color: white; padding: 10px 15px; border: none; cursor: pointer; border-radius: 4px; }
        button:hover { background: #219150; }
        .btn-delete { background: #e74c3c; padding: 5px 10px; text-decoration: none; font-size: 0.8em; }
    </style>
</head>
<body>
    <nav>
        <a href="/">🖥️ Inventario</a>
        <a href="/add">➕ Nuevo Equipo</a>
        <a href="/about">ℹ️ Acerca de</a>
    </nav>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
"""



@app.route('/')
def home():
    # HTML específico de la tabla, inyectado en el tema base
    contenido = """
    {% extends "base" %}
    {% block content %}
        <h1>Inventario de Infraestructura</h1>
        <p>Total de equipos: <strong>{{ inventory|length }}</strong></p>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
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
                    <td style="color: {{ 'green' if item.status == 'active' else 'orange' }}">
                        {{ item.status|upper }}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endblock %}
    """
    # Renderizamos combinando el tema base y el contenido
    return render_template_string(TEMA_BASE.replace('{% block content %}{% endblock %}', contenido), inventory=inventory)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Guardar datos
        new_id = len(inventory) + 1
        inventory.append({
            "id": new_id,
            "name": request.form.get('name'),
            "location": request.form.get('location'),
            "status": request.form.get('status')
        })
        return redirect(url_for('home'))
    
    # HTML del Formulario
    contenido = """
    {% extends "base" %}
    {% block content %}
        <h1>Registrar Nuevo Equipo</h1>
        <form method="POST">
            <label>Nombre del Dispositivo:</label>
            <input type="text" name="name" required placeholder="Ej: Router Cisco 2901">
            
            <label>Ubicación:</label>
            <input type="text" name="location" required placeholder="Ej: Rack 4, Unidad 2">
            
            <label>Estado Operativo:</label>
            <select name="status">
                <option value="active">🟢 Activo</option>
                <option value="maintenance">🟠 Mantenimiento</option>
                <option value="retired">🔴 Retirado</option>
            </select>
            
            <button type="submit">Guardar en Base de Datos</button>
        </form>
    {% endblock %}
    """
    return render_template_string(TEMA_BASE.replace('{% block content %}{% endblock %}', contenido))

@app.route('/about')
def about():
    contenido = """
    {% extends "base" %}
    {% block content %}
        <h1>Acerca del Sistema</h1>
        <p>Sistema desarrollado íntegramente en <strong>Python</strong> para la Evaluación 3.</p>
        <ul>
            <li>Backend: Flask</li>
            <li>Frontend: Jinja2 String Templates</li>
            <li>Container: Docker</li>
        </ul>
    {% endblock %}
    """
    return render_template_string(TEMA_BASE.replace('{% block content %}{% endblock %}', contenido))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
