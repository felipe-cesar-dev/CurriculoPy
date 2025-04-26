import webbrowser
import tempfile

from Controler.ControleRecuperarDados import ControleRecuperarDados


class CurriculoHTML:
    def __init__(self, recuperar: ControleRecuperarDados):
        self.__recuperar = recuperar

    def criar_e_abrir_pagina(self):
        dados = self.__recuperar.selectall()
        html = f"""
            <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                    <style>
                        body{{
                            justify-content: center;
                            background-color: lightblue;
                            display: flex;
                            padding: 0;
                            margin: 0;
                        }}
                        
                        #curriculo{{
                            background-color: lightblue;
                            height: 1095px;
                            width: 900px;
                            display: flex;
                        }}
                
                        #sessaoPrincipal{{
                            display:flex;
                            flex-direction: column;
                            align-items: center;
                            height: 1090px;
                            background-color: rgb(1, 52, 162);
                            width: 290px;
                            border: 2px solid white;
                            margin-left: 0px;
                            border-radius: 10px;
                        }}
                
                        #foto{{
                            width: 200px;
                            height: 200px;
                            background-color: rgba(0, 0, 0, 0.392);
                            border-radius: 50%;
                            border: 2px solid white;
                            margin-top: 10px;
                        }}
                
                        #nomeProf{{
                            color: white;
                        }}
                
                        #nomeProf h3{{
                            margin-top: -15px;
                        }}
                
                        #grupoInfos{{
                            border: 2px solid white;
                            width: 270px;
                            height: 733px;
                            border-radius: 10px;
                            display: flex;
                            flex-direction: column;
                        }}
                
                        #grupoInfos h2{{
                            text-align: center;
                            color: white;
                        }}
                
                        #grupoInfos h4{{
                            margin-left: 10px;
                            color: white;
                            margin-top: -2px;
                        }}
                
                        #grupoInfos div{{
                            border-top: 1px solid white;
                            margin-left: 10px;
                            margin-right: 10px;
                            padding-top: 10px;
                        }}
                        
                        #sessaoInfosAdicionais{{
                            width: 430px;
                            display: flex;
                            flex-direction: column;
                        }}
                
                        .infos{{
                            margin-left: 20px;
                            margin-top: 20px;
                            width: 450px;
                            height: auto;
                            border: 1px solid rgb(58, 58, 58);
                            border-radius: 10px;
                        }}
                
                        .infos h2{{
                            text-align: center;
                        }}
                
                        .infos h4{{
                            text-align: justify;
                            padding: 10px;
                            margin-top: -5px;
                        }}
                
                        .infos div{{
                            border: 1px, solid rgb(58, 58, 58);
                            margin-left: 10px;
                            margin-right: 10px;
                        }}
                
                    </style>
                </head>
                <body>
                    <div id=curriculo>
                        <div id="sessaoPrincipal">
                            <div id="foto"></div>
                            <div id="nomeProf">
                                <h1>Nome</h1>
                                <h3>Profissao</h3>
                            </div>
                            <div id="grupoInfos">
                                <h2>Informações Pessoais:</h2>
                                <h4>Nascimento:</h4>
                                <h4>Nacionalidade:</h4>
                                <h4>Estado Civil:</h4>
                                <div></div>
                                <h2>Informações de Contato:</h2>
                                <h4>Celular:</h4>
                                <h4>E-mail:</h4>
                                <h4>Endereço:</h4>
                                <div></div>
                                <h2>Redes:</h2>
                                <h4>Facebook:</h4>
                                <h4>Instagram:</h4>
                                <h4>Linkedin:</h4>
                            </div>
                        </div>
                        <div id="sessaoInfosAdicionais">
                            <div class="infos">
                                <h2>Um pouco sobre mim:</h2>
                                <div></div>
                                <h4></h4>
                            </div>
                            <div class="infos">
                                <h2>Experiência(s) Profissional(is):</h2>
                                <div></div>
                                <h4></h4>
                            </div>
                            <div class="infos">
                                <h2>Formação Acadêmica:</h2>
                                <div></div>
                                    <h4></h4>
                                </div>
                            <div class="infos">
                                <h2>Cursos:</h2>
                                <div></div>
                                <h4></h4>
                            </div>
                            <div class="infos">
                                <h2>Conhecimentos:</h2>
                                <div></div>
                                <h4>
                                </h4>
                            </div>
                        </div>
                    </div>
                </body>
                <script></script>
                </html>

        """

        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as arquivo:
            arquivo.write(html.encode())
            url = arquivo.name
            webbrowser.open(f"file://{url}")


