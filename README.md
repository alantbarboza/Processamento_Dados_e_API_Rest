# Descrição dos Códigos

Este repositório contém dois scripts Python que realizam operações diferentes: um para obter dados de clima utilizando a API do OpenWeatherMap e outro para processar um arquivo CSV de transações.

## Script para Obter Dados de Clima

### Requisitos

- Python 3.7 ou superior
- Pacotes necessários: aiohttp, python-dotenv

### Configuração

Antes de executar o script, certifique-se de criar um arquivo .env na raiz do projeto com a seguinte variável:

```dotenv
weather_key=your_weather_api_key





--
--
Q1/ETAPA 1:
Automatização de Processamento de Dados CSV

Você recebe um arquivo CSV com informações sobre transações financeiras. Cada linha contém: nome do cliente, valor da transação e data da transação. Sua tarefa é escrever um script Python que leia o arquivo CSV, identifiquetransaçõesacima de um determinado valor (porexemplo, $1000) e as salve em um novo arquivo CSV.

Requisitos:
•	O script deve ser capaz de ler um arquivo CSV chamado transacoes.csv.
•	Identificar transações com valor superior a $1000.
•	Salvar as transações identificada sem um novo arquivochamadotransacoes_altas.csv.

Exemplo de Estrutura do Arquivo CSV que sera utilizado para teste (transacoes.csv):
Nome do Cliente,Valor da Transação,Data da Transação
Cliente A,1200,2023-01-15
Cliente B,800,2023-02-02
Cliente C,1500,2023-03-10
Cliente D,900,2023-04-05


Q2/ETAPA 2:
API Rest e Python

Tarefas:
•	Conexão com a API OpenWeatherMap:
•	Faça uma solicitação GET para a API OpenWeatherMap (https://openweathermap.org/current) para obter informações meteorológicas de uma cidade de sua escolha.
•	Crie uma chave de API para autenticar suas solicitações.
•	Extraia e exiba os seguintes detalhes sobre o clima atual da cidade:
•	Descrição do clima (por exemplo, "ensolarado", "chuvoso", etc.).
•	Temperatura atual em graus Celsius.
