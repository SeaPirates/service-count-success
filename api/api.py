from flask import Flask

app = Flask(__name__)

@app.route('/graphic')
def api():
	return 'Minha Primeira API em Python'
