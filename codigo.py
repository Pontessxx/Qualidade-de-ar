import matplotlib.pyplot as plt
import requests

class AirQualityAnalyzer:
    def __init__(self):
        self.dados = []
        self.meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ags', 'Set', 'Out', 'Nov', 'Dez']
        self.opcao = 0

    def exibir_menu(self):
        print('_' * 30)
        print('\n         AXION GREEN')
        print('_' * 30)
        print('\nBem-vindo ao Analisador de Qualidade do Ar\n')
        print('Opções:')
        print('(1) Inserir dados mensais')
        print('(2) Ver gráfico da qualidade do ar')
        print('(3) Informar região para o banco de dados')
        print('(0) Sair\n')


    def classificar_qualidade_ar(self, ar):
        # Mapear intervalos de poluição para classificações e LEDs/buzzers correspondentes
        classificacoes = {
            (1, 3): ('VERDE', 'Notone'),
            (3, 6): ('AMARELO', 'Notone'),
            (6, 11): ('VERMELHO', 'Tone')
        }
        for intervalo, (led, buzzer) in classificacoes.items():
            if intervalo[0] <= ar < intervalo[1]:
                return led, buzzer

    def inserir_dados(self):
        for i, mes in enumerate(self.meses):
            ar = self.validar_input(f'{mes}:\nMédia mensal da qualidade do ar fornecida pelo sensor: ', 1, 10)
            led, buzzer = self.classificar_qualidade_ar(ar)
            self.dados.append(ar)

    def validar_input(self, prompt, min_value, max_value):
        while True:
            try:
                valor = int(input(prompt))
                if min_value <= valor <= max_value:
                    return valor
                else:
                    print(f"Digite um número entre {min_value} e {max_value}")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

    def plotar_grafico(self):
        plt.plot(self.dados, color='darkcyan', label='Leituras de cada mês')
        plt.title('Qualidade do ar - Anual')
        plt.xlabel('Meses')
        plt.ylabel('Valor')
        plt.xticks(range(12), self.meses)
        plt.yticks(range(11))
        plt.legend()
        plt.show()

    def contar_classificacoes(self):
        # Inicializar contadores para cada classificação
        contagem = {'VERDE': 0, 'AMARELO': 0, 'VERMELHO': 0}
        
        for ar in self.dados:
            led, _ = self.classificar_qualidade_ar(ar)
            contagem[led] += 1
        
        return contagem

    def plotar_grafico_barras(self, contagem):
        classificacoes = list(contagem.keys())
        quantidade = list(contagem.values())
        
        plt.bar(classificacoes, quantidade, color=['green', 'yellow', 'red'])
        plt.title('Distribuição de Classificações da Qualidade do Ar')
        plt.xlabel('Classificação')
        plt.ylabel('Quantidade')
        plt.show()

    def menu_nova_operacao(self):
        print("*-------------------------------*")
        print("	       MENU")
        print("*-------------------------------*")
        print("Escolha uma opção:\n")
        print("(1) Reinserir os dados mensais")
        print("(2) Ver gráfico e encerrar programa")
        print("(3) Informar a região para o banco de dados\n")

    def reinserir_dados(self):
        self.dados = []
        self.inserir_dados()

    def informar_regiao(self):
        print('\n')
        print("*-------------------------------*")
        print("	       CEP                ")
        print("*-------------------------------*")
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

        while self.opcao != 2:
            self.opcao = int(input('Opção: '))
            if self.opcao == 1:
                self.inserir_dados()
            elif self.opcao == 2:
                print('\nGráfico:')
                self.plotar_grafico()
                
                contagem = self.contar_classificacoes()
                self.plotar_grafico_barras(contagem)
                break
                #self.menu_nova_operacao()
            elif self.opcao == 3:
                self.informar_regiao()
            elif self.opcao == 0:
                break
            else:
                print('Opção inválida. Por favor, escolha novamente.')

            self.menu_nova_operacao()

if __name__ == "__main__":
    analyzer = AirQualityAnalyzer()
    analyzer.main()

