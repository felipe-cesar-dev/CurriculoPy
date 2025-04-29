from Controller.ControleAtivacaoInputs import ControleAtivacaoInputs
from Controller.ControleBotoes import ControleBotoes
from Controller.ControleRecuperarDados import ControleRecuperarDados
from Controller.ControleTratarDados import ControleTratarDados
from Model.TratarDados import TratarDados
from View.Botao import Botao
from View.CurriculoHTML import CurriculoHTML
from View.Inputs import Inputs
from View.Labels import Labels
from View.Sessoes import Sessoes
from View.Tela import  Tela
from Model.RecuperarDados import RecuperarDados

recuperardb = RecuperarDados()
recuperar = ControleRecuperarDados(recuperardb)
gerarHTML = CurriculoHTML(recuperar)
clicar = ControleBotoes()
ativacao = ControleAtivacaoInputs()
tratar = TratarDados()
controle = ControleTratarDados(tratar, ativacao)
tratar.limparTodosDados()
labels = Labels()
botao = Botao(clicar, gerarHTML)
inputs = Inputs(labels, controle, botao, ativacao)

sessoes = Sessoes(inputs, botao)
tela = Tela(sessoes, labels, botao)
tela.run()
