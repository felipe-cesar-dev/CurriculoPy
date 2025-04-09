from View.Botao import Botao
from View.Inputs import Inputs
from View.Labels import Labels
from View.Sessoes import Sessoes
from View.Tela import  Tela
from Model.Armazenamento import SQLiteDB

db = SQLiteDB('curriculo.db')
labels = Labels()
inputs = Inputs(labels)
botao = Botao(db)


sessoes = Sessoes(inputs, botao)
tela = Tela(sessoes, labels, botao)
tela.run()
