# -*- coding: utf-8 -*-

from leiloes.db import Base, engine
from leiloes.models import *

Base.metadata.create_all(bind=engine)
