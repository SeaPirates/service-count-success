from flask import json


class Series:

    QUERY_EXERCICIO = 'SELECT ' \
                      'COUNT(quant_acertos) as acertos ' \
                      'FROM metrics.exercicios ' \
                      'WHERE data_registro BETWEEN %s AND %s'

    def __init__(self, mysql):
        self.mysql = mysql

    def metricas(self, params):
        parametros = json.loads(params)
        cursor = self.mysql.connection.cursor()
        cursor.execute(self.QUERY_EXERCICIO, parametros['params'])
        result = json.dumps(cursor.fetchall())
        return result
