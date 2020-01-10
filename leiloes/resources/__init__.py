from flask_restful import Resource
from leiloes.models import Fornecedor, Teste 
from leiloes.db import db_session 
from flask import jsonify


import random

class FornecedorList(Resource):
    def get(self):
        ''' Modelo de Insert '''
        teste = Teste(id=random.randint(1, 100), titulo="asasas", status=9)
        db_session.add(teste)

        teste2 = Teste()
        teste2.id = random.randint(1, 100)
        teste2.titulo = "asasasqw   qwqeweqweqweqweqweqweqwe"
        teste2.status = 9
        db_session.add(teste2)

        db_session.commit()

        ''' Modelo de Consulta '''
        teste = db_session.query(Teste).all()
        def create_item(item):
            return {
            'titulo' : item.titulo,
            'status' : item.status,
        }
        return jsonify({u'results': map(create_item, teste)})
    

        
        # fornecedor = Fornecedor(id=random.randint(1, 100), titulo="asasas", status=9)
        # db_session.add(fornecedor)
        # db_session.commit()
        
                
        
        db_session.close()
        return {'FornecedorList aqui': 'get'}
    
    def post(self):
        req = request.get_json()
        return {'FornecedorList': 'post'}



class FornecedorAPI(Resource):
    def get(self, fornecedor_id):
        return {'Fornecedor': 'get'}
    
    def delete(self, fornecedor_id):
        return {'Fornecedor': 'delete'}

    def put(self, fornecedor_id):
        return {'Fornecedor': 'put'}








class GabaritoLeilaoList(Resource):
    def get(self):
        return {'hello': 'world'}

class GabaritoLeilao(Resource):
    def get(self, gabarito_id):
        return {'hello': 'world'}

class GabaritoItemList(Resource):
    def get(self, gabarito_id):
        return {'hello': 'world'}

class GabaritoItem(Resource):
    def get(self, gabarito_id):
        return {'hello': 'world'}

class LeilaoList(Resource):
    def get(self):
        return {'hello': 'world'}

class Leilao(Resource):
    def get(self, leilao_id):
        return {'hello': 'world'}

class LeilaoItemList(Resource):
    def get(self, leilao_id):
        return {'hello': 'world'}

class LeilaoItem(Resource):
    def get(self, leilao_id, item_id):
        return {'hello': 'world'}

class LeilaoFornecedoresList(Resource):
    def get(self, leilao_id):
        return {'hello': 'world'}

class LeilaoParticipantesList(Resource):
    def get(self, leilao_id):
        return {'hello': 'world'}

class LeilaoLanceList(Resource):
    def get(self, leilao_id):
        return {'hello': 'world'}

class LeilaoLance(Resource):
    def get(self, leilao_id, lance_id):
        return {'hello': 'world'}

class LeilaoAnexoList(Resource):
    def get(self, leilao_id):
        return {'hello': 'world'}

class LeilaoAnexo(Resource):
    def get(self, leilao_id, anexo_id):
        return {'hello': 'world'}
