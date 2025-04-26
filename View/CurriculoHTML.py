import webbrowser
import tempfile
from Controler.ControleRecuperarDados import ControleRecuperarDados

class CurriculoHTML:
    def __init__(self, recuperar: ControleRecuperarDados):
        self.__recuperar = recuperar

    def criar_e_abrir_pagina(self):
        dados = self.__recuperar.selectall('pessoas')
        nome, profissao = dados[0][0], dados[0][1]
        profissao = dados[0][1]
        nascimento, nacionalidade, estadoC = dados[0][2], dados[0][3], dados[0][4]
        celular, email, endereco = dados[0][5], dados[0][6], dados[0][7]

        redes = self.__recuperar.selectall('redes')
        face, insta, linkedin = redes[0][1], redes[0][2], redes[0][3]

        sobremim = self.__recuperar.selectall('sobremim')
        textosobre = sobremim[0][1]

        experiencia = self.__recuperar.selectall('experiencias')
        exp1, exp2, exp3, exp4, exp5 = experiencia[0][1],experiencia[0][2],experiencia[0][3],experiencia[0][4],experiencia[0][5]

        formacoes = self.__recuperar.selectall('formacoes')
        f1, f2, f3, f4, f5 = formacoes[0][1],formacoes[0][2],formacoes[0][3],formacoes[0][4],formacoes[0][5]

        cursos = self.__recuperar.selectall('cursos')
        c1, c2, c3, c4, c5 = cursos[0][1],cursos[0][2],cursos[0][3],cursos[0][4],cursos[0][5]

        conhecimentos = self.__recuperar.selectall('conhecimentos')
        co1, co2, co3, co4, co5 = conhecimentos[0][1],conhecimentos[0][2],conhecimentos[0][3],conhecimentos[0][4],conhecimentos[0][5]

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
                            text-align: center;
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
                                <h2>{nome}</h2>
                                <h3>{profissao}</h3>
                            </div>
                            <div id="grupoInfos">
                                <h2>Informações Pessoais:</h2>
                                <h4>Nascimento: {nascimento}</h4>
                                <h4>Nacionalidade: {nacionalidade}</h4>
                                <h4>Estado Civil: {estadoC}</h4>
                                <div></div>
                                <h2>Informações de Contato:</h2>
                                <h4>Celular: {celular}</h4>
                                <h4>E-mail: {email}</h4>
                                <h4>Endereço: {endereco}</h4>
                                <div></div>
                                <h2>Redes:</h2>
                                <h4>Facebook: {face}</h4>
                                <h4>Instagram: {insta}</h4>
                                <h4>Linkedin: {linkedin}</h4>
                            </div>
                        </div>
                        <div id="sessaoInfosAdicionais">
                            <div class="infos">
                                <h2>Um pouco sobre mim:</h2>
                                <div></div>
                                <h4>{textosobre}</h4>
                            </div>
                            <div class="infos">
                                <h2>Experiência(s) Profissional(is):</h2>
                                <div></div>
                                <ul>
                                    <li>{exp1}</li>
                                    <li>{exp2}</li>
                                    <li>{exp3}</li>
                                    <li>{exp4}</li>
                                    <li>{exp5}</li>
                                </ul>
                            </div>
                            <div class="infos">
                                <h2>Formação Acadêmica:</h2>
                                <div></div>
                                <ul>
                                    <li>{f1}</li>
                                    <li>{f2}</li>
                                    <li>{f3}</li>
                                    <li>{f4}</li>
                                    <li>{f5}</li>
                                </ul>
                                </div>
                            <div class="infos">
                                <h2>Cursos:</h2>
                                <div></div>
                                <ul>
                                    <li>{c1}</li>
                                    <li>{c2}</li>
                                    <li>{c3}</li>
                                    <li>{c4}</li>
                                    <li>{c5}</li>
                                </ul>
                            </div>
                            <div class="infos">
                                <h2>Conhecimentos:</h2>
                                <div></div>
                                <ul>
                                    <li>{co1}</li>
                                    <li>{co2}</li>
                                    <li>{co3}</li>
                                    <li>{co4}</li>
                                    <li>{co5}</li>
                                </ul>
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


