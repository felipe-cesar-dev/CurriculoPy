from Controler.ControleAtivacaoInputs import ControleAtivacaoInputs
from Controler.ControleBotoes import ControleBotoes
from Controler.ControleTratarDados import ControleTratarDados
from Model.TratarDados import TratarDados
from View.Botao import Botao
from View.Inputs import Inputs
from View.Labels import Labels
from View.Sessoes import Sessoes
from View.Tela import  Tela

clicar = ControleBotoes()
ativacao = ControleAtivacaoInputs()
tratar = TratarDados()
controle = ControleTratarDados(tratar, ativacao)
tratar.limparTodosDados()
labels = Labels()
botao = Botao(clicar)
inputs = Inputs(labels, controle, botao, ativacao)

sessoes = Sessoes(inputs, botao)
tela = Tela(sessoes, labels, botao)
tela.run()
