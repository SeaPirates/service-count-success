from flask import json
from src.series.exercicios import Exercicios


class Series:

    def __init__(self):
        self.exercicios = Exercicios()

    def metricas(self, params):

        if (params['banca'] == 'all'):
            result = self.exercicios\
                .select()\
                .where(
                    (self.exercicios.data_registro >= params['date_begin']) &
                    (self.exercicios.data_registro <= params['date_end'])
                ).count()
        else:
            result = self.exercicios \
                .select() \
                .where(
                    (self.exercicios.banca == params['banca']) &
                    (self.exercicios.data_registro >= params['date_begin']) &
                    (self.exercicios.data_registro <= params['date_begin'])
                ).count()

        self.exercicios.close()
        return json.dumps({"result": str(result)})
