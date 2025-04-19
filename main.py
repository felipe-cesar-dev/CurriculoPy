from Controler.ControleAtivacaoInputs import ControleAtivacaoInputs
from Controler.ControleTratarDados import ControleTratarDados
from Model.TratarDados import TratarDados
from View.Botao import Botao
from View.Inputs import Inputs
from View.Labels import Labels
from View.Sessoes import Sessoes
from View.Tela import  Tela


ativacao = ControleAtivacaoInputs()
tratar = TratarDados()
controle = ControleTratarDados(tratar)
tratar.limparTodosDados()
labels = Labels()
botao = Botao()
inputs = Inputs(labels, controle, botao, ativacao)

sessoes = Sessoes(inputs, botao)
tela = Tela(sessoes, labels, botao)
tela.run()
