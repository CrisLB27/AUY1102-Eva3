from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = [
    {"id": 1, "name": "Servidor Dell PowerEdge", "status": "active"},
    {"id": 2, "name": "Switch Cisco Catalyst", "status": "maintenance"},
    {"id": 3, "name": "Firewall Fortinet", "status": "active"}
]

@app.route('/')
def home():
    return jsonify({
        "service": "Inventory-API",
        "version": "1.0.0",
        "status": "running"
    })

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({"count": len(inventory), "items": inventory})

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)