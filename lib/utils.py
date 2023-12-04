
import json
from time import sleep
from datetime import datetime
import os
import pandas as pd

class utils:
    def __init__(self):
      self.opçao = {
            1:  "Ver saldo",
            2: "Adicionar entrada",
            3: "subtrair gastos",
            4: "Visualizar tabela de gastos",
            5: "visualizar tabela de entradas",
            0: "sair"
         }

    def _add_(self, entrada: float):

        # Carregar dados existentes
        with open('lib/cash.json', 'r') as file:
            dados = json.load(file)

        # Verificar se a chave 'saldo' existe no dicionário
        if 'saldo' in dados:
            # Se existir, atualizar o valor de 'saldo'
            dados['saldo'] += entrada
        else:
            # Se não existir, criar a chave 'saldo' com o valor de entrada
            dados['saldo'] = entrada

        # Escrever os dados atualizados no arquivo JSON
        with open('lib/cash.json', 'w') as file:
            json.dump(dados, file, indent=4)


    def _div_(self, entrada: float):

        # Carregar dados existentes
        with open('lib/cash.json', 'r') as file:
            dados = json.load(file)

        # Verificar se a chave 'saldo' existe no dicionário
        if 'saldo' in dados:
            # Se existir, atualizar o valor de 'saldo'
            dados['saldo'] -= entrada
        else:
            # Se não existir, criar a chave 'saldo' com o valor de entrada
            dados['saldo'] = entrada

        # Escrever os dados atualizados no arquivo JSON
        with open('lib/cash.json', 'w') as file:
            json.dump(dados, file, indent=4)



    def _hourDate_(self):
        data_hora_atual = datetime.now()
        # Formatar a data
        data_formatada = data_hora_atual.strftime('%d/%m/%Y')  # Formato: DD/MM/AAAA
        # Formatar a hora
        hora_formatada = data_hora_atual.strftime('%H:%M:%S')
        return  data_formatada, hora_formatada

    def _clear_(self):
        return os.system("cls"), os.system("@echo off")

    def _calc_(self):
        self._clear_()
        data, hour = self._hourDate_()

        novo_dado = {f'[data: {data}] [hour: {hour}]': 0}  # Inicializa um novo dado com o valor zero
        print(f"+{'-' *30}+")
       
        if (entrada := float(input("Digite o valor a ser adicionado: "))):
            print(f"+{'-' *30}+")
        
            try:
                with open('lib/entradas.json', 'r') as file:
                    dados = json.load(file)  # Carrega os dados existentes do arquivo JSON
            except FileNotFoundError:
                dados = {}  # Se o arquivo não existir, cria um novo dicionário vazio

            chave_procurada = f'[data: {data}] [hour: {hour}]'


            if chave_procurada in dados:
                dados[chave_procurada] += entrada  # Adiciona ao valor existente se a chave estiver presente
            else:
                novo_dado[chave_procurada] = entrada  # Cria um novo registro se a chave não estiver presente
                dados.update(novo_dado)  # Adiciona ao dicionário de dados

            with open('lib/entradas.json', 'w') as file:
                json.dump(dados, file, indent=4)
            self._add_(entrada)
            self.contador(f"Valor {entrada} adicionado. Voltando ao menu em: ")  # Escreve os dados atualizados de volta no arquivo JSON

    def _sub_(self):
        self._clear_()
        data, hour = self._hourDate_()

        novo_dado = {f'[data: {data}] [hour: {hour}]': 0}  # Inicializa um novo dado com o valor zero
        print(f"+{'-' *30}+")
        if (entrada := float(input("Digite o valor a ser Subtraido: "))):
            print(f"+{'-' *30}+")

            try:
                with open('lib/gastos.json', 'r') as file:
                    dados = json.load(file)  # Carrega os dados existentes do arquivo JSON
            except FileNotFoundError:
                dados = {}  # Se o arquivo não existir, cria um novo dicionário vazio

            chave_procurada = f'[data: {data}] [hour: {hour}]'

            if chave_procurada in dados:
                dados[chave_procurada] += entrada  # Adiciona ao valor existente se a chave estiver presente
            else:
                novo_dado[chave_procurada] = entrada  # Cria um novo registro se a chave não estiver presente
                dados.update(novo_dado)  # Adiciona ao dicionário de dados

            with open('lib/gastos.json', 'w') as file:
                json.dump(dados, file, indent=4)  # Escreve os dados atualizados de volta no arquivo JSON
            
            self._div_(entrada)
            self.contador(f"Valor {entrada} subtraido. Voltando ao menu em: ")  # Escreve os dados atualizados de volta no arquivo JSON


    
    def _saldo_(self):
        with open('lib/cash.json', 'r') as arquivo_json: dados = json.load(arquivo_json)
        self._clear_()
        if 'saldo' in dados.keys():
            print(f"+{'-' * 30}+")
            print(f"Saldo: [{round(dados['saldo'], 2)}]")
            print(f"+{'-' * 30}+")
            input("Tecle [enter] para voltar ao menu...")
            self.contador("Voltando ao menu em: ")
            return
        else:
            self._clear_()
            print(f"+{'-' * 30}+")
            saldo = float(input("Digite seu saldo: "))
            dados['saldo'] = saldo
            with open('lib/cash.json', 'w') as file:
                json.dump(dados, file, indent=4)



    def _tableGastos_(self):
        self._clear_()

        with open('lib/gastos.json', 'r') as file:
            dados = json.load(file)

        # Criar um DataFrame a partir dos dados do JSON
        df = pd.DataFrame(list(dados.items()), columns=['Timestamp', 'Valor'])

        print(f"+{'-' *46}+")
        print(f"|{'Tabela de Gastos':^{46}}|")
        print(f"+{'-' *46}+")
        # Mostrar o DataFrame formatado
        print(df)
        print(f"+{'-' *46}+")

        # Perguntar ao usuário se deseja criar o arquivo Excel
        if  opcao:= input("Deseja criar um arquivo Excel com esses dados? [(s/n)]: ").lower() == 's':
            nome_arquivo = input("Digite o nome do arquivo Excel (sem extensão): ")
            # Exportar para Excel
            df.to_excel(f"{nome_arquivo}.xlsx", index=False)
            self.contador(f"Arquivo {nome_arquivo}.xlsx criado com sucesso, voltando ao menu:")
        else:
            self.contador("voltando ao menu em:")

    def _tableEntradas_(self):
        self._clear_()

        with open('lib/entradas.json', 'r') as file:
            dados = json.load(file)

        # Criar um DataFrame a partir dos dados do JSON
        df = pd.DataFrame(list(dados.items()), columns=['Timestamp', 'Valor'])

        print(f"+{'-' *46}+")
        print(f"|{'Tabela de Entradas':^{46}}|")
        print(f"+{'-' *46}+")
        # Mostrar o DataFrame formatado
        print(df)
        print(f"+{'-' *46}+")

        # Perguntar ao usuário se deseja criar o arquivo Excel
        if  opcao:= input("Deseja criar um arquivo Excel com esses dados? [(s/n)]: ").lower() == 's':
            nome_arquivo = input("Digite o nome do arquivo Excel (sem extensão): ")
            # Exportar para Excel
            df.to_excel(f"{nome_arquivo}.xlsx", index=False)
            self.contador(f"Arquivo {nome_arquivo}.xlsx criado com sucesso, voltando ao menu:")
        else:
            self.contador("voltando ao menu em:")
            



    def contador(self, msg: str, segundos: int = 3):
            for i in range(segundos):
                min, seg =divmod(segundos-i, 60)
                txt = f"{min:02d}:{seg:02d}" if segundos > 59 else f"{seg:02d}" 
                print(f"{msg} [{txt}] segundos", end="\r")
                sleep(1)
            return


    def _menu_(self):
        print(f"+{'-' *36}+")
        print(f"|{'MENU':^{36}}|")
        print(f"+{'-' *36}+")
        for i, j in self.opçao.items():
         print(f"|{f'[{i}] - {j}':{36}}|")
        print(f"+{'-' *36}+")



         


