# Analisador de Qualidade do Ar - AXION GREEN

## Descrição

O Analisador de Qualidade do Ar - AXION GREEN é uma ferramenta que permite a análise e visualização da qualidade do ar e umidade do ar ao longo dos meses, além de oferecer funcionalidades como estimativa do mês em que a qualidade do ar atingirá um valor desejado.

## Funcionalidades

- Inserir os dados mensais de qualidade do ar e umidade.
- Visualizar gráficos da qualidade do ar e umidade ao longo dos meses.
- Ver gráficos combinados de qualidade do ar e umidade.
- Estimar o mês em que a qualidade do ar atingirá um valor desejado.
- Informar a região para obter detalhes do CEP.
- Sair da aplicação.

## Estimativa do Mês com Base em Valor Desejado

Uma das funcionalidades do Analisador de Qualidade do Ar é a capacidade de estimar o mês em que a qualidade do ar atingirá um valor desejado. Essa estimativa é baseada na técnica de otimização conhecida como Método de Newton-Raphson.

### Como Funciona

A função `estimar_mes_valor(valor_desejado)` utiliza o Método de Newton-Raphson para encontrar uma aproximação do mês em que a qualidade do ar atingirá o valor desejado. A ideia por trás desse método é iterativamente refinar a estimativa inicial do mês, usando informações da derivada da função de qualidade do ar.

O método começa com uma estimativa inicial de mês (geralmente 0) e itera várias vezes, ajustando a estimativa com base na diferença entre o valor desejado e o valor real da qualidade do ar. A derivada da função de qualidade do ar é usada para determinar a taxa de mudança da qualidade do ar em relação ao mês.

### Limitações e Considerações

É importante observar que a estimativa do mês é uma aproximação e depende da qualidade dos dados, da escolha do valor de `h` na função de derivada, do número de iterações e de outros fatores. Portanto, os resultados podem variar com base nas condições reais futuras.

Os usuários devem entender que essa estimativa é baseada em cálculos numéricos e tendências históricas dos dados. Recomenda-se que a estimativa seja interpretada como uma previsão aproximada, não como uma certeza absoluta.

### Exemplo de Uso

```python
valor_desejado = 5  # Substitua pelo valor desejado
mes_estimado = self.estimar_mes_valor(valor_desejado)
print(f"O mês estimado para alcançar a qualidade do ar desejada é: {mes_estimado}")
```
## Créditos e integrantes
- RM 98036 Henrique Pontes Olliveira
- RM 98460 Felipe Capriotti da Silva Santos
- RM 99679 Gustavo Kawamura Christofani
- RM 550908 Vinicius Santos Yamashita de Farias
- RM 99874 Rafael Carvalho Mattos
