from flask import Flask
from flask import request
from src.series.series import Series

app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():
    series = Series()
    return app.response_class(
        response=series.metricas(request.data),
        status=200,
        mimetype='application/json'
    )
