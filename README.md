<h1>Sobre o programa Currículo</h1>
<ul>
    <li>O projeto foi desenvolvido para facilitar a criação de currículos.</li>
    <li>O público alvo é o de pessoas que querem criar um currículo profissional de forma rápida, num programa leve.</li>
    <li>Após preencher alguns ‘inputs’, o usuário poderá gerar uma pré-visualização de um currículo numa página web, adicionar uma foto e baixar o pdf do mesmo.</li>
    <li>O programa permite que o usuário altere as suas informações e gere uma nova visualização do currículo, enquanto o programa estiver aberto</li>

</ul>
<h1>Este projeto foi desenvolvido utilizando as seguintes tecnologias:</h1>
<ul>
    <li>SQLite3 para armazenamento de dados do currículo, como nome, profissão, etc.</li>
    <li>TKinter para a interface do programa.</li>
    <li>Lib 're' para tratamento de dados.</li>
    <li>Libs 'webbrowser' e 'tempfile' para abrir o html presente no código CurriculoHTML.py.</li>
    <li>Existe também, para a conversão do html em pdf, a utilização da lib 'jspdf', do JavaScript, para gerar o pdf do currículo. </li>
</ul>

<h1>Rotina de configuração do aplicativo:</h1>
<ul>
    <li>Será necessária a importação das libs externas para o correto funcionamento do aplicativo.</li></ul>


<h1>Sobre a modularização do código:</h1>
<p>O código desenvolvido foi baseado no padrão MVC, tendo a interface localizada no módulo View, o controle do armazenamento dos dados e as funções dos botões, concentrados na camada Controle, e o armazenamento no banco de dados, tratado na camada Model.  </p>
<p>Foram aplicadas técnicas de arquitetura de software baseadas no SOLID.</p>
<h1>Camada Controller</h1>
<h2>/Controler/ClassesAbstratas/ControleAtivacaoInputsABS.py</h2>
<p>O arquivo contém a classe com os métodos abstratos para gerir a atividade dos botões presentes na interface do usuário. </p>
<h2>/Controler/ControleAtivacaoInputs.py</h2>
<p>O arquivo implementa os métodos da classe mencionada acima. A ideia central é que todos os botões da aplicação estejam em state = 'disabled', enquanto o botão referente ao salvamento do nome do usuário, não seja ativado. Esse botão entra em estado 'disabled', uma vez que haja sucesso no salvamento do nome, mudando para 'normal', os outros botões referentes a 'salvar' e 'gerar currículo'.
</p>
<h2>/Controler/ClassesAbstratas/ControleBotoesABS.py</h2>
<p>A classe no código, descreve métodos para a ativação e desativação dos botões salvar e editar.</p>
<h2>/Controler/ControleBotoes.py</h2>
<p>Esse código implementa os métodos da classe acima, e trata de controlar a ativação e desativação dos botões 'editar' e 'salvar', alternando entre estados. Quando um entra em estado 'normal', o outro entra em 'disabled', permitindo assim alterar alguma informação do usuário, dentro do bd, uma vez que o dado ja tenha sido salvo.</p>
<h2>Controler/ClassesAbstratas/ControleTratarDadosABS.py</h2>
<p>Esse código contém a descrição dos métodos responsáveis pelo tratamento dos dados, e pela ponte entre o que se aciona na View, e o que é armazenado na Model.</p>
<h2>Controler/ControleTratarDados.py</h2>
<p>Esse arquivo contém o código que implementa os métodos da classe acima. Possui métodos para armazenamento de dados por arrays e também, individualmente. Ele trata os dados capturados na View para serem armazenados corretamente no banco de dados. Nele, também há um método para validar um nome digitado, para não ser permitido salvar nomes com caracteres especiais e campo vazio.</p>
<p>Para o correto funcionamento da aplicação, o banco de dados é limpo sempre que uma nova instância dele é executada, permitindo que haja somente uma linha para cada coluna das tabelas no bd. A def salvar_nome é responsável por garantir isso.</p>
<p>A classe necessita que seja instanciada a classe TratarDados, da Model, e passagem de um parâmetro de ativação do botão de salvar nome, quando for clicado</p>
<h2>Controler/ControleRecuperarDados.py</h2>
<p>Contém o código necessário para recuperar dados armazenados bd, e exibí-los no html do currículo.</p>
<p>A ideia central é selecionar todos os dados dentro do bd, e entregar para a classe CurriculoHTML, presente no arquivo com o mesmo nome, para que ela exiba os dados, quando o botão Gerar Currículo for pressionado.</p>
<p>A classe precisa que na sua inicialização seja instanciada a classe RecuperarDados, da Model</p>
<h1>Camada Model</h1>

<h2>/Model/RecuperarDados.py</h2>
<p>Responsável por recuperar os dados armazenados no banco de dados. Que futuramente serão utilizados como passagem de parâmetros para compor o currículo.</p>
<h2>/Model/TratarDadosABS.py</h2>
<p>Contém uma classe com as descrições dos métodos responsáveis pelo armazenamento dos dados no banco de dados, além de um método específico para exclusão de todos os dados das tabelas.</p>
<h2>/Model/TratarDados.py</h2>
<p>Implementa os métodos da classe acima.</p>

<h1>Camada View</h1>
<h2>/View/ClassesAbstratas/BotaoABS.py</h2>
<p>Contém o código com a descrição dos métodos para criar o botão para salvar nome, salvar outros dados e editá-los, e um botão para gerar o html</p>
<h2>/View/Botao.py</h2>
<p>Contém uma classe que implementa os métodos da classe acima. A classe requisita a instanciação das classes ControleBotoes da Controller e CurriculoHTML, da View.</p>
<p>Os botões dessa classe são instanciados dentro da classe Input, na View. É necessária a instanciação das classes de controle de botões, pois ela será responsável por alterar o estado de um botão de 'disabled' para 'normal' e vice-versa, quando clicado. Esse controle de estados é feito por dois métodos internos a def criarBotao, os métodos comandoa e comandob. </p>
<p>O parâmetro 'armazenar' nos métodos self da classe, será tratado na classe Input, onde se faz necessário o armazenamento dos botões 'salvar' para poderem ser mencionados na hora de terem os seus estados alterados.</p>
<p>A instanciação da classe CurrículoHTML faz-se necessária para gerar o html do currículo uma vez que o seu botão seja clicado.</p>

<h2>/View/ClassesAbstratas/InputsABS.py</h2>
<p>Contém o código para a classe que descreve os métodos para criação de 'Entrys' na aplicação.</p>
<h2>/View/Inputs.py</h2>
<p>Contém a classe que implementa a classe acima.</p>
<p>Para o correto funcionamento da classe, será necessária a instanciação das classes Label, ControleTratarDados, Botao e ControleAtivacaoInputs.</p>
<p>Em breve, essa classe terá uma reestruturação, diminuindo a quantidade de código redundante.</p>
<p>De forma geral ela é responsável por exibir os "Entry's" na tela, e instanciar os seus botões e "labels" equivalentes.</p>
<p>Dentro do método inputText, existe um método próprio que aplica o controle de caracteres digitados dentro do Text da aplicação, limitando a 300 caracteres.</p>
<p>O método criarInputsAdicionais, é responsável por gerar na tela os "Entry's" referentes as sessões Cursos, Conhecimentos, Experiências e Formação Acadêmica. Esse método é instanciado uma vez para cada uma dessas sessões, gerando na tela, 5 "Entry's" para a adição de informações ao banco de dados. Faz-se necessária a passagem do parâmetro 'tabela' na instanciação desse método, para determinar, qual tabela do banco de dados armazenará o dado inserido no Entry.</p>
<p>O método buildInputs é responsável por instanciar toda a criação de "Entry's" na tela. Esse método é invocado pela classe Sessoes, na View.</p>
<p>A variável self.__nome = [] serve para armazenar o nome capturado ao clicar no botão que chama o método botaoNome na Botao. Ela será utilizada como ponto de referência para cada dado armazenado nas tabelas do curriculo.db. Ela dirá que o nome armazenado nela é a chave primária no banco de dados. O nome sempre estará na posição [0] da variável. </p>
<p>self.__armazenar_botoes = [] serve para armazenar os botões da aplicação, exceto os 'Editar'. Essa variável se faz necessária para haver o controle dos estados dos botões.</p>
<p>self.__ativar = 'disabled' é responsável por ter o seu valor alterado ('normal') quando necessário para mudar o estado de um botão ou layout.</p>
<p>self.__entradas e self.__inputs retornam um array que armazenam o estado dos Entry's e Text da aplicação. Por padrão, esses widgets ficam desativados na execução da aplicação, exceto o widget para o nome. Uma vez que o nome é salvo, todos os widgets dentro desse array, mudam o seu estado para 'normal'. Esse estado também é alterado quando uma informação é guardada no bd, uma vez que o botão de salvar ou editar é clicado.</p>
<h2>/View/ClassesAbstratas/LabelsABS.py</h2>
<p>Contém o código da classe para descrever os métodos de criação de labels espalhados pela aplicação.</p>
<h2>/View/Labels.py</h2>
<p>Implementa os métodos da classe acima.</p>
<h2>/View/ClassesAbstratas/SessoesABS.py</h2>
<p>Contém o código da classe que descreve os métodos para a criação de sessões na aplicação.</p>
<h2>/View/Sessoes.py</h2>
<p>Implementa os métodos da classe acima.</p>
<p>Para o correto funcionamento da aplicação, será necessária a instanciação das classes Inputs e Botao </p>
<h2>/View/Tela.py</h2>
<p>Contém o código para executar a interface da aplicação.</p>
<p>É necessária a instanciação de Sessao, Label e Botao, para o seu correto funcionamento.</p>
<h2>View/CurriculoHTML.py</h2>
<p>Contém o código HTML, com estilização e utilização de JavaScript, para gerar a visualização do currículo numa página Web. Nesse código, existe a possibilidade de ser adicionada uma foto no currículo e também o seu salvamento em pdf.</p>
<h2>/curriculo.db</h2>
<p>Contém as tabelas e colunas responsáveis pelo armazenamento dos dados capturados pelos Entry's da aplicação.</p>
<h2>/main.py</h2>
<p>Executa a aplicação.</p>