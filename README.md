# Trabalho de Simulação de Rede P2P
Este trabalho consiste na implementação de um programa em Python que simula uma rede P2P não estruturada e permite realizar buscas por recursos utilizando diferentes algoritmos de busca.

## Descrição do Problema
O objetivo deste programa é criar uma estrutura de dados representando uma rede P2P não estruturada a partir de um arquivo de configuração fornecido como entrada. A rede P2P é composta por nós que possuem recursos, e o programa permite realizar buscas por esses recursos utilizando diferentes algoritmos de busca.

## Funcionalidades do Programa
O programa possui as seguintes funcionalidades:

1. Leitura do arquivo de configuração: O programa lê um arquivo de configuração que descreve a rede P2P e os recursos mantidos pelos nós.

2. Criação do grafo: Com base nas informações do arquivo de configuração, o programa cria um grafo que representa a rede P2P. Os nós do grafo representam os nós da rede e as arestas representam as conexões entre os nós.

3. Validação da rede: O programa verifica se a rede criada é conexa, se os limites de vizinhos de cada nó são respeitados e se não há nós sem recursos.

4. Algoritmos de busca: O programa implementa diferentes algoritmos de busca, incluindo busca por inundação, busca por passeio aleatório e busca informada. Esses algoritmos são executados no grafo criado e permitem buscar recursos mantidos pelos nós da rede.

5. Testes comparativos: O programa realiza testes comparativos entre os diferentes algoritmos de busca em diferentes configurações de redes P2P. Os resultados dos testes são registrados, incluindo o número total de mensagens trocadas na rede até que a localização do recurso seja encontrada ou a busca termine sem encontrar o recurso.

## Como Executar o Programa
1. Instale o Python 3 em seu sistema, se ainda não estiver instalado.

2. Faça o download dos arquivos do projeto.

3. Execute o programa fornecendo um arquivo de configuração como argumento. Por exemplo:

```
python main.py input_example.txt
```
Substitua config.txt pelo caminho do seu arquivo de configuração.

4. Os resultados das buscas e as informações sobre o grafo serão exibidos na saída do programa.

## Requisitos de Implementação
O programa utiliza a linguagem Python e as seguintes bibliotecas:

- NetworkX: Biblioteca para criação, manipulação e visualização de grafos.
- Outras bibliotecas (a serem listadas, se houver)
## Estrutura do Projeto
O projeto possui a seguinte estrutura de diretórios:

```
├── main.py
├── file_util.py
├── graph_util.py
├── algorithms.py
├── input_example.txt
├── README.md
└── ...
```
- *main.py*: Arquivo principal que inicia a execução do programa.
- *file_util.py*: Classe para leitura do arquivo de configuração.
- *graph_util.py*: Classe para criação e manipulação do grafo.
- *algorithms.py*: Implementação dos algoritmos de busca.
- *input_example.txt*: Arquivo de configuração que descreve a rede P2P.
- *README.md*: Documentação do projeto.
- 
## Contribuidores
- [Tiago Ary Castelo](https://github.com/tiagoAry15)
- [Luiz Miguel Gomes Cunha](https://github.com/LuizMiguel1905)


