from peewee import *
import os

db = MySQLDatabase(
    "metrics",
    host=os.environ['MYSQL_HOST'],
    port=int(os.environ['MYSQL_PORT']),
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASS']
)

class Exercicios(Model):
    id = PrimaryKeyField()
    banca = CharField()
    data_registro = DateField()
    quant_questoes = IntegerField()
    quant_error = IntegerField()
    quant_acertos = IntegerField()
    user_id = IntegerField()

    def close(self):
        db.close()

    class Meta:
        database = db