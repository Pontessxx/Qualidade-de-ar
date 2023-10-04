# Analisador de Qualidade do Ar - Axion Green

Bem-vindo ao Analisador de Qualidade do Ar da Axion Green. Esta ferramenta foi projetada para monitorar, analisar e estimar a qualidade do ar e a umidade ao longo do ano. Com uma variedade de funcionalidades, você pode facilmente inserir dados, visualizar gráficos informativos e estimar valores desejados.

## Funcionalidades

### 1. Inserção de Dados Mensais

Utilize o menu "Inserir Dados Mensais" para adicionar informações sobre a qualidade do ar e umidade de cada mês. Insira valores de 1 a 10 para representar a qualidade do ar e a umidade.

### 2. Visualização de Gráficos

Explore uma série de gráficos para visualizar seus dados:

- **Qualidade do Ar ao Longo dos Meses:** Acompanhe as variações mensais da qualidade do ar.
- **Variação da Umidade:** Observe como a umidade se altera durante o ano.
- **Comparação Qualidade do Ar e Umidade:** Veja ambos os fatores em um único gráfico.
- **Relação entre Qualidade do Ar e Umidade:** Analise a correlação entre essas variáveis.

### 3. Estimativa do Mês com Base em Valor Desejado

Digite um valor de qualidade do ar desejado (de 1 a 10) para prever o mês em que ele poderá ser alcançado. A estimativa leva em consideração a taxa de mudança da qualidade do ar.

### 4. Estimativa de Meses para Valores de 0 a 10

Receba uma estimativa dos meses para uma variedade de valores de qualidade do ar (0 a 10). Visualize os meses em que esses valores podem ocorrer.

### 5. Informações da Região via CEP

Insira um CEP para acessar informações locais, como logradouro, bairro, cidade e estado.

## Nova Implementação

Aprimoramos o método de estimativa de mês para qualidade do ar, utilizando cálculos mais precisos baseados na derivada da série temporal da qualidade do ar. A derivada oferece insights sobre as mudanças ao longo do tempo, possibilitando uma estimativa mais precisa.

Ao calcular a derivada da qualidade do ar em relação aos meses, identificamos períodos de aumento ou diminuição acentuados. Isso melhora a precisão da previsão para atingir valores desejados, considerando as tendências sazonais.

## Requisitos

Certifique-se de ter o Python instalado. Você pode precisar instalar as seguintes bibliotecas:

- matplotlib
- numpy
- requests
- pandas

Instale-as usando:
```bash
pip install [nome da biblioteca]

```


## Utilidade da Derivada

A derivada ajuda a compreender as mudanças da qualidade do ar ao longo do tempo. Sua magnitude indica rapidez e direção da mudança. Por exemplo:

- Derivada positiva: Melhoria ao longo do tempo.
- Derivada negativa: Deterioração ao longo do tempo.
- Magnitude reflete a velocidade da mudança.

Ao visualizar o gráfico da derivada em relação aos meses, você identifica tendências e picos de mudança rápida. Isso apoia decisões em políticas ambientais e planejamento urbano.

## Método de Newton para Estimar Mês

Utilizamos o método de Newton para estimar o mês desejado. O método iterativo aproxima raízes de funções.

### Funcionamento

1. Calculamos a derivada da qualidade do ar ao longo dos meses.
2. Iniciamos com um mês (por exemplo, 0) e iteramos para encontrar a raiz da função.
3. Iterações continuam até encontrar a raiz ou atingir máximo de iterações.

### Vantagens

O método de Newton é eficiente para raízes de funções complexas. Considera a taxa de mudança, possibilitando estimativas precisas.

### Limitações

Pode não convergir se a função for complexa. Precisão depende do valor inicial.

## Uso do Pandas e Docstrings

Neste projeto, utilizamos a biblioteca Pandas para manipulação e análise de dados. O Pandas nos permite criar DataFrames para organizar os dados mensais e calcular médias anuais.

As docstrings foram incluídas para descrever a funcionalidade de cada função e método. Isso torna o código mais legível e facilita a compreensão das operações realizadas em cada parte do programa.

## Créditos e Integrantes

- RM 98036 Henrique Pontes Olliveira
- RM 98460 Felipe Capriotti da Silva Santos
- RM 99679 Gustavo Kawamura Christofani
- RM 550908 Vinicius Santos Yamashita de Farias
- RM 99874 Rafael Carvalho Mattos


