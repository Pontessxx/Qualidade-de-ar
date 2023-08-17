# Analisador de Qualidade do Ar e Umidade

Este é um programa Python que permite analisar a qualidade do ar ao longo dos meses, exibindo gráficos e informações relevantes. O programa permite inserir dados mensais de qualidade do ar e umidade, visualizar gráficos, calcular derivadas e até mesmo obter informações de regiões com base em CEPs.

## Créditos e integrantes
- RM 98036 Henrique Pontes Olliveira
- RM 98460 Felipe Capriotti da Silva Santos
- RM 99679 Gustavo Kawamura Christofani
- RM 550908 Vinicius Santos Yamashita de Farias
- RM 99874 Rafael Carvalho Mattos


## Funcionalidades

- **Inserir Dados Mensais:** Insira os dados mensais de qualidade do ar e umidade para cada mês do ano.
- **Ver Gráficos:** Visualize gráficos que mostram a qualidade do ar e a umidade ao longo dos meses.
- **Calcular Derivadas:** Calcule e visualize as derivadas numéricas da qualidade do ar em relação aos meses.
- **Informar Região:** Informe um CEP para obter informações sobre a região correspondente.

## Implementação da Derivada

A derivada é calculada utilizando a biblioteca NumPy. No código, o método `calcular_derivada(self, dados)` é responsável por calcular a derivada numérica dos dados de qualidade do ar em relação aos meses. Aqui está como funciona:

```python
def calcular_derivada(self, dados):
    derivada = np.gradient(dados)
    return derivada
```

1. A função `np.gradient(dados)` é usada para calcular a derivada numérica dos dados. Ela calcula a variação entre valores adjacentes nos dados e divide pela variação entre os meses adjacentes, o que resulta na taxa de mudança da qualidade do ar em relação aos meses.

2. A derivada calculada é retornada pelo método.

   
## Utilidade da Derivada

A derivada é útil para entender como a qualidade do ar está mudando ao longo do tempo. Ela fornece informações sobre a taxa de variação da qualidade do ar em relação aos meses. Por exemplo:

- Se a derivada é positiva, significa que a qualidade do ar está aumentando, indicando uma melhoria ao longo do tempo.
- Se a derivada é negativa, significa que a qualidade do ar está diminuindo, indicando uma deterioração ao longo do tempo.
- A magnitude da derivada indica a rapidez com que a qualidade do ar está mudando.

Ao visualizar o gráfico da derivada em relação aos meses, é possível identificar tendências de melhoria ou piora da qualidade do ar, bem como picos de mudança rápida. Isso pode ser útil para tomar decisões informadas sobre políticas ambientais e planejamento urbano.

## Requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema.

## Como Usar

1. Clone este repositório para o seu computador ou faça o download do código-fonte.
2. Abra um terminal e navegue até o diretório onde o código está localizado.
3. Execute o programa digitando `python nome_do_arquivo.py` (substitua `nome_do_arquivo.py` pelo nome do arquivo do programa).
4. Siga as instruções no menu para inserir dados, visualizar gráficos ou obter informações sobre uma região.
5. caso necessite instalar a biblioteca `matplotlib` basta digitar no terminal:
6. caso necessite instalar a biblioteca `numpy`basta digitar no terminal:
```bash
pip install matplotlib
pip install numpy
````
6. Após isso, inicie o codigo novamente.

## Exemplo de plotagem de grafico:
![image](https://github.com/Pontessxx/Qualidade-de-ar/assets/126187491/c5e0bc61-b36a-42e8-a52d-c108b95c7989)
![image](https://github.com/Pontessxx/Qualidade-de-ar/assets/126187491/0ae13b89-30b9-46c2-9e3d-d5b0f952679e)
![image](https://github.com/Pontessxx/Qualidade-de-ar/assets/126187491/0baeb66f-9063-4d5c-a035-3936f9a7da46)
![image](https://github.com/Pontessxx/Qualidade-de-ar/assets/126187491/befc8724-3dbb-4ac5-bb17-ae46b3664e0c)


## Licença

Este projeto está licenciado sob a Licença [Nome da Licença] - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
