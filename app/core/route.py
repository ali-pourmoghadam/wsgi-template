from core.init import *


@app.route('/')
def hello():
    return 'Hello, this is a Flask application using uWSGI!'



@app.route('/api' , methods=['POST'])
def rec():
         return jsonify({'message': 'Data received and processed successfully', 'processed_data': 'dummy response ...'}), 200


def hello():
    return 'Hello, this is a Flask application using uWSGI!'


