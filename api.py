from flask import Flask, request, render_template
from flask_cors import CORS
import json
from personality import best_goods_per_personality


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@app.route('/api/', methods=['POST'])
def api_system():
    content = request.json
    data = dict()
    
    data["result"] = best_goods_per_personality(content["personality"])

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run()