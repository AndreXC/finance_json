
from lib.utils import utils

class finance:
    def __init__(self):
        self.finance = utils()


    def _main_(self):
        while True:
            self.finance._clear_()
            self.finance._menu_()
            try:
                
                if (op:= int(input("Digite uma opção: "))) in [1, 2, 3,4,5, 0]:
                    match op:
                        case 1:
                            self.finance._saldo_()
                        case 2:
                            self.finance._calc_()
                        case 3:
                            self.finance._sub_()
                        case 4:
                            self.finance._tableGastos_()
                        case 5:
                            self.finance._tableEntradas_()
                        case 0:
                            self.finance.contador("Desligando em: ")
                            exit()
                else:
                    self.finance._clear_()
                    self.finance.contador("Opção inválida, Voltando ao Menu Em: ")
            except ValueError:
                self.finance.contador("Erro, opções disponíveis [1, 2, 3, 0]. Tente novamente em: ")












if __name__ =="__main__":
    start = finance()
    start._main_()


