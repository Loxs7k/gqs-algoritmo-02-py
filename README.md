# Conversor de Real para Dólar (com IOF)

Repositório: **gqs-algoritmo-02-py**

Programa em Python que calcula quanto custa, em reais, comprar uma
determinada quantidade de dólares, já incluindo o **IOF de 6%**
(imposto cobrado sobre operações de câmbio no Brasil).


## Nível 1: Criação e Código Fonte

# Arquivo do programa

O código está em [`main.py`](./main.py).

# Como executar


# 1. Clone o repositório
git clone https://github.com/Loxs7k/gqs-algoritmo-02-py.git
cd gqs-algoritmo-02-py

# 2. Execute com Python 3
python main.py


O programa vai exibir a cotação do dólar utilizada e pedir que você
digite quantos dólares deseja comprar.


## Nível 2: Documentação e Explicação do Algoritmo

# O que o código faz?

O programa informa a cotação do dólar sendo usada, pede ao usuário
quantos dólares ele deseja comprar e calcula o valor total a ser pago
em reais, já com o IOF de 6% embutido no cálculo.

# Detalhamento do código

Elemento  O que faz 

class CurrencyConverter` | Agrupa os dados e a lógica da conversão em um só lugar (cotação, taxa de IOF e o cálculo) 
dolla e iof: Atributos de classe: guardam a cotação do dólar (**3.10**) e o multiplicador do IOF (**1.06**, ou seja, 6% a mais) 
calc(quantity): Recebe a quantidade de dólares e retorna o valor total em reais: **(quantity * dolla) * iof ***
input(): Captura a quantidade de dólares digitada pelo usuário no terminal 
float(...): Converte o texto digitado em número decimal 
f-strings (f"...{var:.2f}"): Formatam os números exibidos com 2 casas decimais 
if __name__ == "__main__": Garante que main() só roda quando o arquivo é executado diretamente 

# Lógica do cálculo:

python
def calc(quantity):
    return (quantity * CurrencyConverter.dolla) * CurrencyConverter.iof


Primeiro multiplica a quantidade de dólares pela cotação (valor "puro"
em reais); depois multiplica esse resultado por **1.06**, que já embute
o acréscimo de 6% do IOF.

# Exemplo de saída

Entrada: 12


What is the dollar price? 3.10
How many dollars will be bought? 
12
Amount to be paid in reais = 39.43


## Nível 3: Toque Profissional

# Resumo técnico

Característica Detalhe 

Linguagem  Python 3 
Bibliotecas externas Nenhuma (apenas recursos nativos) 
Entrada de dados Via **input()** no terminal 
Cotação do dólar considerada R$ 3,10 (fixa, definida como atributo de classe) 
Taxa de IOF considerada 6% (representada como multiplicador **1.06**) 

# Possíveis melhorias futuras

1- Buscar a cotação do dólar em tempo real via API (ex: AwesomeAPI, ExchangeRate-API).
2- Validar entradas negativas ou inválidas com **try/except**.
3- Permitir escolher entre diferentes moedas (EUR, GBP, etc.).

# Sobre o Autor

Desenvolvido por **Lorran Rodrigues**, estudante de TI na Una Contagem,
como parte da atividade de Garantia da Qualidade de Software / Gestão
e Qualidade de Software, ministrada pelo professor Daniel Henrique
Matos de Paiva.