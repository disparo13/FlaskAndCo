from flask import Flask, jsonify

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
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET']) # http://127.0.0.1:5000/store/some_name
def getStore(name):
    pass

# GET /store
@app.route('/store')
def getStores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def createItemInStore(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def getItemsInStore():
    pass

@app.route('/')
def home():
    return "Hello User!"


app.run(port=5000)
