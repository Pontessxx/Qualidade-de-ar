# Analisador de Qualidade do Ar - Axion Green

Bem-vindo ao Analisador de Qualidade do Ar, uma ferramenta desenvolvida pela Axion Green para ajudar a monitorar e analisar a qualidade do ar e a umidade em diferentes meses do ano. O programa permite a inserção de dados mensais, visualização de gráficos informativos e estimativa de meses com base em valores de qualidade desejados.

## Funcionalidades

### 1. Inserir Dados Mensais

Você pode inserir os dados mensais de qualidade do ar e umidade utilizando o menu "Inserir Dados Mensais". Insira valores de 1 a 10 para a qualidade do ar e a umidade.

### 2. Visualizar Gráficos

O programa oferece diversos gráficos para visualizar os dados:

- **Gráfico de Qualidade do Ar:** Visualize a variação da qualidade do ar ao longo dos meses.
- **Gráfico de Umidade do Ar:** Veja como a umidade do ar varia durante o ano.
- **Gráficos Combinados:** Compare a qualidade do ar e a umidade no mesmo gráfico.
- **Gráfico de Qualidade do Ar por Umidade:** Verifique a relação entre a qualidade do ar e a umidade.

### 3. Estimar Mês com Base em Valor Desejado

Com essa função, você pode inserir um valor desejado de qualidade do ar (de 1 a 10) e o programa estimará o mês em que esse valor pode ser alcançado. A estimativa é baseada na taxa de mudança da qualidade do ar.

### 4. Estimar Meses com Base em Valores de 0 a 10

Esse recurso oferece uma estimativa dos meses em que a qualidade do ar poderia variar de 0 a 10. Ele fornece uma lista de valores de qualidade do ar desejados e os meses estimados para alcançá-los.

### 5. Informar Região para o Banco de Dados

Você pode inserir um CEP (Código de Endereçamento Postal) e o programa verificará informações relacionadas a essa região, como logradouro, bairro, cidade e estado.

## Nova Implementação

Recentemente, foi aprimorado o método de estimar o mês com base em um valor desejado de qualidade do ar. Agora, o programa utiliza métodos de cálculo mais precisos para determinar o mês estimado, considerando a taxa de mudança da qualidade do ar ao longo dos meses.

## Requisitos

Certifique-se de ter o Python instalado em sua máquina. Você também pode precisar instalar as seguintes bibliotecas:

- matplotlib
- numpy
- requests

Você pode instalá-las usando o seguinte comando:
```bash
pip install [nome da biblioteca]
```

## Créditos e integrantes
- RM 98036 Henrique Pontes Olliveira
- RM 98460 Felipe Capriotti da Silva Santos
- RM 99679 Gustavo Kawamura Christofani
- RM 550908 Vinicius Santos Yamashita de Farias
- RM 99874 Rafael Carvalho Mattos

## Finalidade do projeto
Esse projeto foi desenvolvido pela Axion Green como parte de nossa iniciativa para promover uma melhor compreensão da qualidade do ar e seu impacto em nossa saúde e meio ambiente. Esperamos que essa ferramenta seja útil para você em sua busca por informações sobre qualidade do ar.
