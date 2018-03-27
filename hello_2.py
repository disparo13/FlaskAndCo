from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Cool Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# From server perspective:
# POST - used to receive data
# GET - used to send data back
# PUT - make sure something is there
# DELETE - remove something

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def createStore():
    requestData = request.get_json()
    newStore = {
        'name': requestData['name'],
        'items': []
    }
    stores.append(newStore)
    return jsonify(newStore)

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET']) # http://127.0.0.1:5000/store/some_name
def getStore(name):
    # Iterate over stores
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'No store was found.'})
    # if the store name matches, return it
    # if none match, return an error


# GET /store
@app.route('/store')
def getStores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def createItemInStore(name):
    requestData = request.get_json()
    for store in stores:
        if store['name'] == name:
            newItem = {
                'name': requestData['name'],
                'price': requestData['price']
            }
            store['item'].append(newItem)
            return jsonify(store)
    return jsonify({'message': 'No store was found.'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def getItemsInStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify( {'items': store['items']} )
    return jsonify({'message': 'No store was found.'})

@app.route('/')
def home():
    return "Hello User!"


app.run(port=5000)
