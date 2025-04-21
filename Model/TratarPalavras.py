from Model.ClassesAbstratas.TratarPalavrasABS import ControleLengthABS


class ControleLength(ControleLengthABS):
    def __init__(self):
        super().__init__()
        pass

    def verificarNome(self, palavra):
        try:
            if len(palavra) == 0 or palavra =='':
                print('Digite algo')
                return
        except:
            print('a')
