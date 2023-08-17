import matplotlib.pyplot as plt
import requests
import numpy as np
class AirQualityAnalyzer:
    def __init__(self):
        self.dados_ar = []
        self.dados_umidade = []
        self.meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ags', 'Set', 'Out', 'Nov', 'Dez']
        self.opcao = 0

    def exibir_menu(self):
        print('_' * 30)
        print('\n         AXION GREEN')
        print('_' * 30)
        print('\nBem-vindo ao Analisador de Qualidade do Ar\n')
        print('Opções:')
        print("(1) Inserir os dados mensais")
        print("(2) Ver gráfico da qualidade do ar")
        print("(3) Ver gráfico da umidade do ar")
        print("(4) Ver gráficos de qualidade de ar e umidade combinados")
        print("(5) Informar a região para o banco de dados")
        print("(6) Informar a região para o banco de dados")
        print('(0) Sair\n')

    def classificar_qualidade(self, valor):
        # Mapear intervalos de poluição para classificações e LEDs/buzzers correspondentes
        classificacoes = {
             (1, 3): ('VERDE', 'Notone'),
             (3, 6): ('AMARELO', 'Notone'),
             (6, 11): ('VERMELHO', 'Tone')
        }
        for intervalo, (led, buzzer) in classificacoes.items():
            if intervalo[0] <= valor < intervalo[1]:
                return led, buzzer

    def validar_input(self, prompt, valor_minimo, valor_maximo):
        while True:
            try:
                valor = int(input(prompt))
                if valor_minimo <= valor <= valor_maximo:
                    return valor
                else:
                    print(f"Digite um número entre {valor_minimo} e {valor_maximo}")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

    def inserir_dados(self):
         for i, mes in enumerate(self.meses):
            print(f'---  [{mes}]  ---')
            ar = self.validar_input(f'\nQualidade de ar: ', 1, 10)
            umidade = self.validar_input(f'Umidade do ar: ', 1, 10)
            print('\n')
            
            led, buzzer = self.classificar_qualidade(ar)
            self.dados_ar.append((ar, led))
            self.dados_umidade.append(umidade)

    def calcular_derivada(self, dados):
        derivada = np.gradient(dados)
        return derivada

    def plotar_grafico_qualidade(self):
        plt.plot([ar for ar, _ in self.dados_ar], color='darkcyan', label='Qualidade do ar')
        plt.title('Qualidade do ar - Anual')
        plt.xlabel('Meses')
        plt.ylabel('Valor')
        plt.xticks(range(12), self.meses)
        plt.yticks(range(11))
        plt.legend()
        
        plt.show()
        self.plotar_grafico_barras()

    def plotar_grafico_barras(self):
        classificacoes = {'VERDE': 0, 'AMARELO': 0, 'VERMELHO': 0}  # Corrigir as classificações aqui

        for _, led in self.dados_ar:
            classificacoes[led] += 1

        classificacoes_nomes = list(classificacoes.keys())
        quantidade = list(classificacoes.values())

        plt.bar(classificacoes_nomes, quantidade, color=['green', 'yellow', 'red'])
        plt.title('Distribuição de Classificações da Qualidade do Ar')
        plt.xlabel('Classificação')
        plt.ylabel('Quantidade')
        plt.show()
    

    def plotar_grafico_umidade(self):
        plt.plot(self.dados_umidade, color='blue', label='Umidade do ar')
        plt.title('Umidade do ar - Anual')
        plt.xlabel('Meses')
        plt.ylabel('Valor')
        plt.xticks(range(12), self.meses)
        plt.yticks(range(15))
        plt.legend()
        plt.show()

    def plotar_graficos_combinados(self):
        plt.plot([ar for ar, _ in self.dados_ar], color='darkcyan', label='Qualidade do ar')
        plt.plot(self.dados_umidade, color='blue', label='Umidade do ar')
        plt.title('Qualidade e Umidade do ar - Anual')
        plt.xlabel('Meses')
        plt.ylabel('Valor')
        plt.xticks(range(12), self.meses)
        plt.legend()
        plt.show()

    def plotar_grafico_qualidade_por_umidade(self):
        qualidade_numeros = [ar for ar, _ in self.dados_ar]
        umidade = self.dados_umidade

        plt.scatter(umidade, qualidade_numeros, color='darkcyan')
        plt.title('Relação entre Qualidade do Ar e Umidade do Ar')
        plt.xlabel('Umidade do Ar')
        plt.ylabel('Qualidade do Ar')
        plt.xticks(range(1, 13))
        plt.yticks(range(1, 13))
        plt.grid()
        plt.show()

    def plotar_grafico_derivada_qualidade(self):
        qualidade_numeros = [ar for ar, _ in self.dados_ar]
        derivada_ar = self.calcular_derivada(qualidade_numeros)

        plt.plot(derivada_ar, color='orange', label='Derivada da Qualidade do ar')
        plt.title('Derivada da Qualidade do ar')
        plt.xlabel('Meses')
        plt.ylabel('Taxa de Mudança')
        plt.xticks(range(12), self.meses)
        plt.legend()
        plt.show()

    def menu_nova_operacao(self):
        print('\n')
        print("_________________________________")
        print("	       MENU")
        print("_________________________________")
        print("Escolha uma opção:\n")
        print("(1) Reinserir os dados mensais")
        print("(2) Ver gráfico da qualidade do ar")
        print("(3) Ver gráfico da umidade do ar")
        print("(4) Ver gráficos de qualidade de ar e umidade combinados")
        print("(5) Ver gráfico de qualidade de ar por umidade")
        print("(6) Ver gráfico com derivada")
        print("(7) Informar a região para o banco de dados")
        print("(0) Sair\n")

    def informar_regiao(self):
        print('\n')
        print("_________________________________")
        print("	       CEP                ")
        print("_________________________________")
        cep = input("Digite o CEP da região: ")
        self.verificar_cep(cep)

    def verificar_cep(self, cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            endereco = response.json()
            print("\n[ CEP encontrado ]\n")
            print(f"CEP: {endereco['cep']}")
            print(f"Logradouro: {endereco['logradouro']}")
            print(f"Complemento: {endereco['complemento']}")
            print(f"Bairro: {endereco['bairro']}")
            print(f"Cidade: {endereco['localidade']}")
            print(f"Estado: {endereco['uf']}")
            print('\n')
        else:
            print("CEP não encontrado.")

    def main(self):
        self.exibir_menu()

        while self.opcao != 8:
            self.opcao = int(input('Opção: '))
            print('\n')
            if self.opcao == 1:
                self.inserir_dados()
            elif self.opcao == 2:
                self.plotar_grafico_qualidade()
            elif self.opcao == 3:
                self.plotar_grafico_umidade()
            elif self.opcao == 4:
                self.plotar_graficos_combinados()
            elif self.opcao == 5:
                self.plotar_grafico_qualidade_por_umidade()
            elif self.opcao == 6:
                self.plotar_grafico_derivada_qualidade()
            elif self.opcao == 7:
                self.informar_regiao()
            elif self.opcao == 0:
                break
            else:
                print('Opção inválida. Por favor, escolha novamente.')

            self.menu_nova_operacao()

if __name__ == "__main__":
    analyzer = AirQualityAnalyzer()
    analyzer.main()
