# Linear Equations Solver

Este projeto é uma aplicação gráfica simples para resolver sistemas de equações lineares. Através de uma interface amigável construída com Tkinter, o usuário pode definir o número de equações, inserir os coeficientes e constantes, e obter a solução do sistema.

## Estrutura do Projeto

```
   linear-equations-solver
├── src
│ |
│ └── solver.py # Lógica para resolver sistemas de equações lineares
├── main.exe # Executaval para rodar o projeto
├── main.py # Ponto de entrada da aplicação (inicia a interface gráfica e a logica)
└── README.md # Documentação do projeto
```


## Como Executar a Aplicação

1. Clone o repositório para sua máquina local.
2. Navegue até o diretório do projeto.
3. Execute o programa usando Python:

```bash
python src/main.py
```

4. Outra maneira seria executar o arquivo main.exe

# Como usar o APP

1.Informe o número de equações do sistema (máximo de 26, pois as variáveis são representadas pelas letras do alfabeto).
2.Clique em Confirmar para gerar os campos para inserir os coeficientes das variáveis e os termos constantes.
3.Preencha os coeficientes e constantes de cada equação.
4.Para um coeficiente omitido, o sistema assume valor 1.
5.Caso queira inserir o coeficiente -1, basta colocar -.
6.Clique em Resolver para calcular a solução.
7.O resultado será exibido na área de texto abaixo, mostrando o valor de cada variável.

## Exemplo
Formato de Entrada
Para um sistema como:

```
   2x + 3y = 5
   4x + y  = 11
```

Sera necessario selecionar como 2 e iremos informar nos campos da seguinte maneira. 

``` 
   2	3	=	5
-----------------------
   4	1	=	11
```

# Lógica de Resolução

*O sistema lê os coeficientes das variáveis e os termos constantes fornecidos pelo usuário.
*Constrói uma matriz dos coeficientes e um vetor dos termos constantes.
*Usa um método numérico para resolver o sistema linear (implementado em solver.py).
*Exibe as soluções correspondentes às variáveis x, y, z, ... conforme a ordem das equações.

# Observações 

*A aplicação usa apenas a biblioteca padrão do Python, com Tkinter para a interface gráfica.
*O projeto é modularizado para facilitar manutenção, separando a interface (app.py), a lógica de resolução (solver.py) e o ponto de entrada (main.py).
*O número máximo de variáveis/equações suportado é 26, correspondendo às letras do alfabeto.