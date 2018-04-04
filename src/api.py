from flask import Flask
from src.series.series import Series
import os
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASS']
app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_PORT'] = int(os.environ['MYSQL_PORT'])
mysql = MySQL(app)

@app.route('/graphic', methods=['POST'])
def api():
    teste = Series(mysql)
    return app.response_class(
        response=teste.metricas(),
        status=200,
        mimetype='application/json'
    )
