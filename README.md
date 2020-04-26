# Cov-ODCMSP

Cov-ODCMSP é uma atividade da disciplina AEDII do curso de Sistemas de Informação da EACH-USP. A intenção da pesquisa é processar os dados da pesquisa Origem Destino (OD) do Metrô de São Paulo a fim de estimar a transmissão da Covid-19 na RMSP (região metropolitana de SP).

## Arquivos

O arquivo da pesquisa está em formato CSV; Cada registro na tabela possui dados sobre uma viagem: dados pessoais do entrevistado (idade, renda etc.), motivo da viagem, coordenadas da origem, coordenadas do destino, coordenadas dos pontos de transferência etc.

Acesse o repositório completo em: https://drive.google.com/drive/folders/1CPD4MBurkI-bCT4xVM3723vXJstCsCkf?usp=sharing

Acesse a legenda em: https://drive.google.com/file/d/1-FmV70hx-IkloPp8f0M9pY9PsljfTXqU/view?usp=sharing

# Primeira tarefa

A primeira tarefa consiste em organizar os dados sendo necessário, criar uma classe ou estrutura Local com os seguintes atributos:

coordenada x

coordenada y

frequentadores.

Os primeiros são inteiros que indicam as coordenadas do lugar, o segundo é um arranjo de inteiros que indica os ids das pessoas que passam por aquele lugar. 

# Segunda Tarefa

A segunda tarefa é construir um histograma do número de pessoas que frequentam cada lugar mencionado na pesquisa. Ou seja, um gráfico cujo eixo x é a quantidade de lugares e o eixo y o número de pessoas que frequentam (quantos lugares são frequentados por um único entrevistado, quantos são frequentados por 2, por 3 e assim por diante).

# Metodologia

A atividade está sendo realizada em python3, com utilização das bibliotecas Pandas e Matplotlib
