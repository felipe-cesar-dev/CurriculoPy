import webbrowser
import tempfile
from Controler.ControleRecuperarDados import ControleRecuperarDados
from tkinter import messagebox

class CurriculoHTML:
    def __init__(self, recuperar: ControleRecuperarDados):
        self.__recuperar = recuperar

    def criar_e_abrir_pagina(self):
        try:
            dados = self.__recuperar.selectall('pessoas')
            nome, profissao = dados[0][0], dados[0][1]
            profissao = dados[0][1]
            celular, email, endereco = dados[0][2], dados[0][3], dados[0][4]
            nascimento, estadoC, nacionalidade = dados[0][5], dados[0][6], dados[0][7]
            redes = self.__recuperar.selectall('redes')
            face, insta, linkedin = redes[0][1], redes[0][2], redes[0][3]
            sobremim = self.__recuperar.selectall('sobremim')
            experiencia = self.__recuperar.selectall('experiencias')
            formacoes = self.__recuperar.selectall('formacoes')
            cursos = self.__recuperar.selectall('cursos')
            conhecimentos = self.__recuperar.selectall('conhecimentos')

            html = f"""
                <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Document</title>
                        <script src="https://unpkg.com/jspdf@latest/dist/jspdf.umd.min.js"></script>
                        <script src="https://unpkg.com/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
                        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
                        <style>
                            body{{
                                justify-content: center;
                                background-color: lightblue;
                                display: flex;
                                padding: 0;
                                margin: 0;
                            }}
                            
                            #salvar-pdf{{
                                height: 60px;
                                border: 1px solid white;
                                color: white;
                                border-radius: 10px;
                                background-color: rgb(1, 52, 162);
                                cursor: pointer;
                            }}
                            
                            #salvar-pdf:hover{{
                                background-color: white;
                                color:rgb(1, 52, 162);
                                transition: 0.5s;
                                border: 1px solid rgb(1, 52, 162);
                            }}
                            
                            #curriculo{{
                                background-color: lightblue;
                                height: 1800px;
                                width: 900px;
                                display: flex;
                            }}
                    
                            #sessaoPrincipal{{
                                display:flex;
                                flex-direction: column;
                                align-items: center;
                                height: 1400px;
                                background-color: rgb(1, 52, 162);
                                width: 290px;
                                border: 2px solid white;
                                margin-left: 0px;
                            }}
                    
                            #foto{{
                                width: 200px;
                                height: 200px;
                                background-color: rgba(0, 0, 0, 0.392);
                                border-radius: 50%;
                                border: 2px solid white;
                                margin-top: 10px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                            }}
                    
                            #nomeProf{{
                                color: white;
                                text-align: center;
                                margin-left:10px;
                                margin-right:10px;
                            }}
                    
                            #nomeProf h3{{
                                margin-top: -15px;
                            }}
                    
                            #grupoInfos{{
                                border: 2px solid white;
                                width: 270px;
                                height: 900px;
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
                                margin-left: 70px;
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
                                margin-top: -15px;
                                padding-left: 15px;
                                padding-right: 30px;
                            }}
                            
                            .p{{
                                 font-family: Arial, Helvetica, sans-serif;
                                 color: white;
                                 margin-top: -15px;
                                 margin-left: 11px;
                            }}
                            
                            .infos li{{
                                margin-left: -20px
                            }}
                    
                            .infos div{{
                                border: 1px, solid rgb(58, 58, 58);
                                margin-left: 10px;
                                margin-right: 10px;
                            }}
                            
                            .custom-file-upload {{
                                display: inline-block;
                                padding: 6px 12px;
                                cursor: pointer;
                                color: white;
                                font-size: 60px;
                                display: flex;
                                justify-content: center;
                            }}
                            
                            .custom-file-upload:hover{{
                                color: lightgray;
                                transition: 0.5s;
                            }}
                    
                        </style>
                    </head>
                    <body>
                        <div id=curriculo>
                            <div id="sessaoPrincipal">
                                <div id="foto">
                                    <label for="selecionar-foto" class="custom-file-upload">
                                        <i class="fa-solid fa-file-arrow-up"></i>
                                    </label>
                                    <input type="file" id="selecionar-foto" accept="image/*" style="display: none;">
                                </div>
                                <div id="nomeProf">
                                    <h2>{nome}</h2>
                                    <h3>{profissao}</h3>
                                </div>
                                <div id="grupoInfos">
                                    <h2>Informações Pessoais:</h2>
                                    <h4>Nascimento: </h4> <p class = 'p'>{nascimento}</p>
                                    <h4>Nacionalidade: </h4> <p class = 'p'>{nacionalidade}</p>
                                    <h4>Estado Civil: </h4> <p class = 'p'>{estadoC}</p>
                                    <div></div>
                                    <h2>Informações de Contato:</h2>
                                    <h4>Celular: </h4> <p class = 'p'>{celular}</p>
                                    <h4>E-mail: </h4> <p class = 'p'>{email}</p>
                                    <h4>Endereço: </h4><p class = 'p'>{endereco}</p>
                                    <div></div>
                                    <h2>Redes:</h2>
                                    <h4>Facebook: </h4> <p class = 'p'>{face}</p>
                                    <h4>Instagram: </h4> <p class = 'p'>{insta}</p>
                                    <h4>Linkedin: </h4> <p class = 'p'>{linkedin}</p>
                                </div>
                            </div>
                            <div id="sessaoInfosAdicionais">
                                <div class="infos">
                                    <h2>Um pouco sobre mim:</h2>
                                    <div></div>
                                    {self.__recuperar.criar_h(sobremim)}
                                </div>
                                <div class="infos">
                                    <h2>Experiência(s) Profissional(is):</h2>
                                    <div></div>
                                    <ul>
                                        {self.__recuperar.criar_li(experiencia)}
                                    </ul>
                                </div>
                                <div class="infos">
                                    <h2>Formação Acadêmica:</h2>
                                    <div></div>
                                    <ul>
                                        {self.__recuperar.criar_li(formacoes)}
                                    </ul>
                                    </div>
                                <div class="infos">
                                    <h2>Cursos:</h2>
                                    <div></div>
                                    <ul>
                                        {self.__recuperar.criar_li(cursos)}
                                    </ul>
                                </div>
                                <div class="infos">
                                    <h2>Conhecimentos:</h2>
                                    <div></div>
                                    <ul>
                                        {self.__recuperar.criar_li(conhecimentos)}
                                    </ul>
                                </div>
                            </div>
                        </div>
                        
                        <button id="salvar-pdf"><h2><i class="fa-solid fa-file-arrow-down"></i> Baixar Currículo</h2></button>
                        <script>
                                document.getElementById("selecionar-foto").addEventListener("change", function(event) {{
                                const arquivo = event.target.files[0];
                                const reader = new FileReader();
                                reader.onload = function(event) {{
                                    const imagem = document.createElement("img");
                                    imagem.src = event.target.result;
                                    imagem.style.width = "100%";
                                    imagem.style.height = "100%";
                                    imagem.style.objectFit = "cover";
                                    imagem.style.borderRadius = "50%";
                                    document.getElementById("foto").innerHTML = "";
                                    document.getElementById("foto").appendChild(imagem);
                                }};
                                reader.readAsDataURL(arquivo);
                            }});
                            document.getElementById("salvar-pdf").addEventListener("click", function() {{
                                html2canvas(document.getElementById("curriculo")).then(canvas => {{
                                    const imgData = canvas.toDataURL('image/png');
                                    const pdf = new jspdf.jsPDF('p', 'mm', 'a4');
                                    const imgWidth = 210; // largura da página A4 em mm
                                    const imgHeight = (canvas.height * imgWidth) / canvas.width;
                                    pdf.addImage(imgData, 'PNG', 0, 0, imgWidth, imgHeight);
                                    pdf.save("curriculo.pdf");
                                }});
                            }});
                        </script>
                    </body>
                    </html>
                    
            """
            self.gerarHTML(html)
        except IndexError as e:
            messagebox.showerror("Erro", "Por favor, salve todos os campos antes de continuar.")

    def gerarHTML(self, html):
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as arquivo:
            arquivo.write(html.encode())
            url = arquivo.name
            webbrowser.open(f"file://{url}")





