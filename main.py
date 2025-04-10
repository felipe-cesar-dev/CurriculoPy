from Model.TratarDados import TratarDados
from View.Botao import Botao
from View.Inputs import Inputs
from View.Labels import Labels
from View.Sessoes import Sessoes
from View.Tela import  Tela



tratar = TratarDados()
labels = Labels()
inputs = Inputs(labels, tratar)
botao = Botao()


sessoes = Sessoes(inputs, botao)
tela = Tela(sessoes, labels, botao)
tela.run()
