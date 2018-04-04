from flask import json


class Series:

    def __init__(self, mysql):
        self.mysql = mysql

    def metricas(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM metrics.bancas')
        result = json.dumps(cursor.fetchall())
        return result
