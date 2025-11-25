from flask import Flask, render_template

app = Flask(__name__)

inventory = [
    {"id": 1, "name": "Servidor Dell PowerEdge", "status": "active", "location": "Rack A"},
    {"id": 2, "name": "Switch Cisco Catalyst", "status": "maintenance", "location": "Rack B"},
    {"id": 3, "name": "Firewall Fortinet", "status": "active", "location": "Perímetro"}
]

@app.route('/')
def home():
    return render_template('inventory.html', title='Inventario de Servidores', inventory=inventory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
