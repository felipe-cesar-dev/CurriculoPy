import webbrowser
import tempfile

texto = 'Olá'
class CurriculoHTML:
    def __init__(self):
        pass

    def criar_e_abrir_pagina(self):
        texto = 'Olá'
        html = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>
                    <h1>{texto}</h1>
                </body>
                </html>
        """

        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as arquivo:
            arquivo.write(html.encode())
            url = arquivo.name
            webbrowser.open(f"file://{url}")
