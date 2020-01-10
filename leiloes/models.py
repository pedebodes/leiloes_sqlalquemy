# -*- coding: utf-8 -*-

from leiloes.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Teste(Base):
    __tablename__ = 'testes'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    status = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return "{}:{}".format(self.id, self.titulo)


class Requisitante(Base):
    __tablename__ = 'requisitantes'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(300))
    status = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return "{}:{}".format(self.id, self.titulo)

class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(300))
    status = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return "{}:{}".format(self.id, self.titulo)

class GabaritoLeilao(Base):
    __tablename__ = 'leilao_gabaritos'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(300))
    status = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return "{}:{}".format(self.id, self.titulo)

class GabaritoAtributos(Base):
    __tablename__ = 'atributos_gabaritos'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(300))
    status = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return "{}:{}".format(self.id, self.titulo)

# class Leilao(Base):
#     __tablename__ = 'leiloes'

#     id = Column(Integer, primary_key=True)
#     titulo = Column(String(300))
#     status = Column(Integer, nullable=False, default=0)

#     requisitante_id = Column(Integer, ForeignKey('requisitantes.id'), nullable=True)
#     requisitante = relationship("Requisitante", back_populates="leiloes")

#     gabarito_id = Column(Integer, ForeignKey('leiloes.id'), nullable=True)
#     gabarito = relationship("GabaritoLeilao", back_populates="leiloes")

#     def __repr__(self):
#         return "{}:{}".format(self.id, self.titulo)

# class LeilaoItem(Base):
#     __tablename__ = 'leilao_itens'

#     id = Column(Integer, primary_key=True)
#     titulo = Column(String(300))
#     status = Column(Integer, nullable=False, default=0)

#     leilao_id = Column(Integer, ForeignKey('leiloes.id'))
#     leilao = relationship("Leilao", back_populates="itens")

#     def __repr__(self):
#         return "{}:{}".format(self.id, self.titulo)

# class LeilaoConvidado(Base):
#     __tablename__ = 'leilao_convidados'

#     id = Column(Integer, primary_key=True)
#     titulo = Column(String(300))
#     status = Column(Integer, nullable=False, default=0)

#     leilao_id = Column(Integer, ForeignKey('leiloes.id'))
#     leilao = relationship("Leilao", back_populates="convidados")

#     fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
#     fornecedor = relationship("Fornecedor", back_populates="leiloes_convidados")

#     def __repr__(self):
#         return "{}:{}".format(self.id, self.titulo)

# class Lance(Base):
#     __tablename__ = 'leilao_lances'

#     id = Column(Integer, primary_key=True)
#     titulo = Column(String(300))
#     status = Column(Integer, nullable=False, default=0)

#     leilao_id = Column(Integer, ForeignKey('leiloes.id'))
#     leilao = relationship("Leilao", back_populates="lances")

#     def __repr__(self):
#         return "{}:{}".format(self.id, self.titulo)

# class LanceItem(Base):
#     __tablename__ = 'leilao_lance_itens'

#     id = Column(Integer, primary_key=True)
#     titulo = Column(String(300))
#     status = Column(Integer, nullable=False, default=0)

#     lance_id = Column(Integer, ForeignKey('leilao_lances.id'))
#     lance = relationship("Leilao", back_populates="items")

#     leilao_id = Column(Integer, ForeignKey('leiloes.id'))
#     leilao = relationship("Leilao", back_populates="lances")

#     leilao_item_id = Column(Integer, ForeignKey('leilao_itens.id'))
#     leilao_item = relationship("LeilaoItem", back_populates="lances")

#     def __repr__(self):
#         return "{}:{}".format(self.id, self.titulo)
