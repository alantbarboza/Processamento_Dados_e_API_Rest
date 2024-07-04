import csv
import logging

# Configuração de logging para registrar erros         
logging.basicConfig(filename='erro_log.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Nome dos arquivos
arquivo_entrada = 'transacoes.csv'
arquivo_saida = 'transacoes_altas.csv'

# Função principal para processar o arquivo CSV
def processar_csv(arquivo_entrada, arquivo_saida, limite=1000):
    try:
        logging.info(f"Iniciando processamento do arquivo: {arquivo_entrada}")
        
        with open(arquivo_entrada, mode='r', newline='', encoding='latin1') as arquivo_csv:
            ler_csv = csv.DictReader(arquivo_csv)
            # Verifica se o arquivo contém as colunas esperadas
            nomes_dos_campos = ler_csv.fieldnames
            if not nomes_dos_campos or 'Nome do Cliente' not in nomes_dos_campos or 'Valor da Transação' not in nomes_dos_campos or 'Data da Transação' not in nomes_dos_campos:
                logging.error('Arquivo CSV nao contem as colunas esperadas.')
                return

            with open(arquivo_saida, mode='w', newline='', encoding='latin1') as arquivo_saida_csv:
                escrever = csv.DictWriter(arquivo_saida_csv, fieldnames=nomes_dos_campos)
                escrever.writeheader()

                contagem_transacoes_altas = 0

                for linha in ler_csv:
                    try:
                        valor_transacao = float(linha['Valor da Transação'])
                        if valor_transacao > limite:
                            escrever.writerow(linha)
                            contagem_transacoes_altas += 1
                    except ValueError as erro:
                        logging.error(f"Erro ao converter valor da transacao: {linha['Valor da Transação']} - {erro}")
                    except KeyError as erro:
                        logging.error(f"Erro ao acessar coluna do CSV: {erro}")

                logging.info(f"Processamento concluído. Transações acima de {limite}: {contagem_transacoes_altas}")
                print(f"Processamento concluido. Transacoes acima de {limite}: {contagem_transacoes_altas}")

    except FileNotFoundError as erro:
        logging.error(f"Arquivo nao encontrado: {erro}")
    except Exception as erro:
        logging.error(f"Erro inesperado: {erro}")

# Executa o processamento do CSV
processar_csv(arquivo_entrada, arquivo_saida)
