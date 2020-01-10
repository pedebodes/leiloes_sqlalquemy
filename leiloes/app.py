# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from leiloes.db import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

from leiloes.resources import *

api.add_resource(FornecedorList, '/fornecedor/')
api.add_resource(FornecedorAPI, '/fornecedor/<int:fornecedor_id>/')

api.add_resource(GabaritoLeilaoList, '/gabarito-leilao/')
api.add_resource(GabaritoLeilao, '/gabarito-leilao/<int:gabarito_id>/')

api.add_resource(GabaritoItemList, '/gabarito-item/')
api.add_resource(GabaritoItem, '/gabarito-item/<int:gabarito_id>/')

api.add_resource(LeilaoList, '/leilao/')
api.add_resource(Leilao, '/leilao/<int:leilao_id>/')

api.add_resource(LeilaoItemList, '/leilao/<int:leilao_id>/item/')
api.add_resource(LeilaoItem, '/leilao/<int:leilao_id>/item/<int:item_id>/')

api.add_resource(LeilaoFornecedoresList, '/leilao/<int:leilao_id>/fornecedores/')

api.add_resource(LeilaoParticipantesList, '/leilao/<int:leilao_id>/participantes/')

api.add_resource(LeilaoLanceList, '/leilao/<int:leilao_id>/lance/')
api.add_resource(LeilaoLance, '/leilao/<int:leilao_id>/lance/<int:lance_id>/')

api.add_resource(LeilaoAnexoList, '/leilao/<int:leilao_id>/anexo/')
api.add_resource(LeilaoAnexo, '/leilao/<int:leilao_id>/anexo/<int:anexo_id>/')
