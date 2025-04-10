from Controler.ControleTratarDadosABS import ControleTratarDadosABS
from Model.TratarDadosABS import TratarDadosABS

class ControleTratarDados(ControleTratarDadosABS):
    def __init__(self, tratar: TratarDadosABS):
        super().__init__()
        self.__tratar = tratar

    def salvar_dados(self, array, nome):
        array.clear()
        array.append(nome.get())
        print(array)
        self.__tratar.salvar_nome(array[0])
