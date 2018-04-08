from flask import Flask
from flask import request
from flask import json
from src.series.series import Series
from src.validade_auth import ValidadeAuth

app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():

    params = json.loads(request.data)

    validar_auth = ValidadeAuth()

    isValid = validar_auth.validar(params['auth'])

    try:
        if (isValid['result']['validate']):
            series = Series()
            return app.response_class(
                response=series.metricas(params['params']),
                status=200,
                mimetype='application/json'
            )
        else:
            return app.response_class(
                response=json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": "metricas",
                        "result": json.dumps(
                            {
                                "status": "502",
                                "status": isValid['result'],
                                "message": "token invalido"
                            }
                        )
                    }
                ),
                status=502,
                mimetype='application/json'
            )
    except:
        return app.response_class(
            response=json.dumps(
                {
                    "jsonrpc": "2.0",
                    "id": "metricas",
                    "result": json.dumps(isValid['result'])
                }
            ),
            status=200,
            mimetype='application/json'
        )





