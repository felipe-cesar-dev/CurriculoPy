<h1>Sobre o programa Currículo</h1>
<ul>
    <li>O projeto foi desenvolvido para facilitar a criação de currículos.</li>
    <li>O público alvo é o de pessoas que querem criar um currículo profissional de forma rápida, em um programa leve.</li>
    <li>Após preencher alguns inputs, o usuário poderá gerar uma pré-visualização de um currículo numa página web, adicionar uma foto e baixar o pdf do mesmo.</li>
    <li>O programa permite que o usuário altere suas informações e gere uma nova visualização do currículo, enquanto o programa estiver aberto</li>

</ul>
<h1>Este projeto foi desenvolvido utilizando as seguintes tecnologias:</h1>
<ul>
    <li>SQLite3 para armazenamento de dados do currículo, como nome, profissão, etc...</li>
    <li>TKinter para a interface do programa.</li>
    <li>Lib 're' para tratamento de dados.</li>
    <li>Libs webbrowser e tempfile para abrir o html presente no código CurriculoHTML.py.</li>
    <li>Existe também, para a conversão do html em pdf, a utilização da lib 'jspdf', do JavaScript, para gerar o pdf do currículo. </li>
</ul>

<h1>Rotina de configuração do aplicativo:</h1>
<ul>
    <li>Será necessária a importação das libs externas para o correto funcionamento do aplicativo.</li>

</ul>
<h1>Sobre a modularização do código:</h1>
<p>O código desenvolvido foi baseado no padrão MVC, tendo a interface localizada no módulo View, o controle do armazenmento dos dados e as funções dos botões, concentrados na camada Controle, e o armazenamento no banco de dados, tratado na camada Model.  </p>
<p>Foram aplicadas técnicas de arquitetura de software baseadas no SOLID.</p>
<h2>/Controler/ClassesAbstratas/ControleAtivacaoInputsABS.py</h2>
<p>O arquivo contém a classe com os métodos abstratos para gerenciar a atividade dos botoes presentes na interface do usuário. </p>
<h2>/Controler/ControleAtivacaoInputs.py</h2>
<p>O arquivo implementa os métodos da classe mencionada acima. A ideia central é que todos os botões da aplicação estejam em state = 'disabled', enquanto o botao referente ao salvamento do nome do usuário, não seja ativado. Esse botão entra em estado 'disabled', uma vez que haja sucesso no salvamento do nome, mudando para 'normal', os outros botões referentes a 'salvar' e 'gerar curriculo'.
</p>
<h2>/Controler/ClassesAbstratas/ControleBotoesABS.py</h2>
<p>A classe no código, descreve métodos para a ativação e desativação dos botões salvar e editar.</p>
<h2>/Controler/ControleBotoes.py</h2>
<p>Esse código implementa os métodos da classe acima, e trata de controlar a ativação e desativação dos botoes 'editar' e 'salvar', alternando entre estados. Quando um entra em estado 'normal', o outro entra em 'disabled', permitindo assim alterar alguma informação do usuário, dentro do bd, uma vez que o dado ja tenha sido salvo.</p>
<h2>Controler/ClassesAbstratas/ControleTratarDadosABS.py</h2>
<p>Esse código contém a descrição dos métodos responsáveis pelo tratamento dos dados, e pela ponte entre o que se aciona na View, e o que é armazenado na Model.</p>
<h2>Controler/ControleTratarDados.py</h2>
<p>Esse arquivo contém o código que implementa os métodos da classe acima. Possui métodos para armazenamento de dados através de arrays e também, individualmente. Ele trata os dados capturados na View para que sejam armazenados corretamente no banco de dados. Nele, também há um método para validar um nome digitado, para que não seja permitido salvar nomes com caracteres especiais e campo vazio.</p>
<p>Para o correto funcionamento da aplicação, o banco de dados é limpado sempre que uma nova instância dele é executada, permitindo que haja somente uma linha para cada coluna das tabelas no bd. A def salvar_nome é responsável por garantir isso.</p>
<p>A classe necessita que seja instanciada a classe TratarDados, da Model, e passagem de um parâmetro de ativação do botão de salvar nome, quando for clicado</p>
<h2>Controler/ControleRecuperarDados.py</h2>
<p>Contém o código necessário para recuperar dados armazendos bd, e exibí-los no html do currículo.</p>
<p>A ideia central é selecionar todos os dados dentro do bd, e entregar para a classe CurriculoHTML, presente no arquivo com o mesmo nome, para que ela exiba os dados, quando o botão Gerar Currículo for pressionado.</p>
<p>A classe precisa que em sua inicialização seja instaciada a classe RecuperarDados, da Model</p>