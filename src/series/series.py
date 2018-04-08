from flask import json
from src.series.exercicios import Exercicios
import datetime


class Series:

    def __init__(self):
        self.exercicios = Exercicios()

    def metricas(self, params):
        json_params = json.loads(params)

        if (json_params['params']['banca'] == 'all'):
            result = self.exercicios\
                .select()\
                .where(
                    (self.exercicios.data_registro >= datetime.date(json_params['params']['date_begin'])) &
                    (self.exercicios.data_registro <= datetime.date(json_params['params']['date_end']))
                ).count()
        else:
            result = self.exercicios \
                .select() \
                .where(
                    (self.exercicios.banca == json_params['params']['banca']) &
                    (self.exercicios.data_registro >= datetime.date(json_params['params']['date_begin'])) &
                    (self.exercicios.data_registro <= datetime.date(json_params['params']['date_end']))
                ).count()

        self.exercicios.close()
        return json.dumps({"result": str(result)})
