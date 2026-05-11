import pandas as pd
import os
import datetime

# Criando um DataFrame vazio com a estrutura final do Arquivo Consolidado
colunas =['Segmento', 'Pais', 'Produto', 'Qtde de Unidades Vendidas', 'Preço Unitário',	'Valor Total',	
          'Desconto', 'Valor Total c/ Desconto', 'Custo Total','Lucro', 'Data', 'Mês', 'Ano']

consolidado = pd.DataFrame(columns=colunas)

# Busca os arquivos a serem consolidados
caminho = os.getcwd()
diretorio = caminho + ("\\planilhas")
arquivos = os.listdir(diretorio)

# Realiza a consolidação dos arquivos Excel
for arq_excel in arquivos:

    if arq_excel.endswith('.xlsx'):
        dados_arquivo = arq_excel.split('-')
        segmento = dados_arquivo[0]
        pais = dados_arquivo[1].replace('.xlsx','')

        try:
            df = pd.read_excel(f'planilhas\\{arq_excel}')
            df.insert(0,'Segmento',segmento)
            df.insert(1,'Pais',pais)
            consolidado = pd.concat([consolidado,df])
            
        except:
            with open('log_erros.txt','a') as arq_log:
                arq_log.write(f'Erro ao tentar consolidar o arquivo: "{arq_excel}".\n')
    else:
        with open('log_erros.txt','a') as arq_log:
                arq_log.write(f'O arquivo "{arq_excel}" não é um arquivo Excel válido!\n')

print("Arquivos consolidados com sucesso!!")

# Exportando o arquivo consolidado para um arquivo Excel
data_now = datetime.datetime.now()

consolidado.to_excel(f"Report-Consolidado-{data_now.strftime('%d-%m-%Y')}.xlsx",
                     index=False,
                     sheet_name='Report Consolidado')