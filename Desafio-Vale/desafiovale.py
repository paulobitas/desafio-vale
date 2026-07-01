from re import search

import pandas as pd
from pathlib import Path
import os

def inicializar():

     # Buscar local de trabalho do usuário
    path_central, path_saida = __define_path()

    path_arquivo_apontamento = Path("Base de Dados/datasets/datasets/apontamentos/")
    path_arquivo_telemetria = Path("Base de Dados/datasets/datasets/telemetria/")

    # Relação de meses dos arquivos de telemetria
    mes_arquivos = ["jan", "feb", "mar", "abr", "may", "jun"]


    def menu():
        print(f"Desafio Vale - Menu")
        option = int(input(f"1 - telemetria por mês\n" +
                        "2 - Alarmes (implementar)\n" +
                        "3 - Apontamentos\n" +
                        "4 - Dados Gerais (implementar)\n" +
                        "0 - Sair (implementar)"))
        

        while True:
            match option:
                case 1:
                    print("Opção 1 selecionada: telemetria por mês")

                    # Criar planilhas de telemetria por mês
                    telemetria_mensal(mes_arquivos, path_arquivo_telemetria, path_saida)

                    break
                case 2: 
                    pass

                case 3:
                    
                    print("Opção 3 selecionada: apontamentos")

                    # Criar planilha de apontamentos
                    apontamento(path_arquivo_apontamento, path_saida)
                    break

                case 4:
                    pass

                case 0: break

        pass 


    menu()
    


    


def __fill_telemetry_sheets(dataframe, nome_aba, path_saida, mes):
    
    #with pd.ExcelWriter(f"{path_saida}/dados_telemetria.xlsx", engine = "openpyxl", mode = "a") as writer:
    #    # Preencher a planilha com os dados do DataFrame
    #    dataframe.to_excel(f"{path_saida}/dados_telemetria.xlsx", sheet_name=nome_aba)

    writer = pd.ExcelWriter(f"{path_saida}/dados_telemetria_{mes}.xlsx", engine = "xlsxwriter")
    dataframe.to_excel(writer, sheet_name = nome_aba)
    writer.close()

    return print(f"Dados de {mes} preenchidos com sucesso na planilha!")

def telemetria_mensal(mes_arquivos, path_arquivo_telemetria, path_saida):

    I = 0

    while I < len(mes_arquivos):
        
        arquivo_telemetria = Path(f"{path_arquivo_telemetria}/telemetry_{mes_arquivos[I]}.parquet")
        df_telemetria = pd.read_parquet(f"{arquivo_telemetria}").head(1000)

        __fill_telemetry_sheets(df_telemetria, f"telemetria_{mes_arquivos[I]}", path_saida, mes_arquivos[I])

        del df_telemetria
        del arquivo_telemetria
        I += 1
    
    return print("Planilhas preenchidas com sucesso!")


def apontamento(path_arquivo_apontamento, path_saida):

    arquivo_apontamento = Path(f"{path_arquivo_apontamento}")

    df_apontamento = pd.read_parquet(f"{path_arquivo_apontamento}//desenvolver_apontamentos.parquet").head(100)

    writer = pd.ExcelWriter(f"{path_saida}/desenvolver_apontamentos_parquet.xlsx", engine = "xlsxwriter")
    df_apontamento.to_excel(writer, sheet_name = "apontamentos")
    writer.close()

    return f"Arquivo de apontamentos preenchido com sucesso na planilha!"





def __define_path():
    try: 
        chosen_path = int(input("Escolha o caminho do projeto (1 - Serviço, 2 - Casa, 0 - Sair): "))
        print('oi')
        print(chosen_path)

        while(chosen_path in {1,2,0}):

            print("inside while")

            match chosen_path:

                case 1: # Serviço 
                    endereco_central = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/")
                    endereco_saida = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/saida/")
                    print("1")
                    return endereco_central, endereco_saida

                case 2: # Casa
                    endereco_central = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/") # Editar
                    endereco_saida = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/saida/") # Editar
                    print("2")
                    return endereco_central, endereco_saida
                    

                case 0:
                    print("Saindo do programa...")
                    print(0)
                    break

                case _:
                    print("Escolha inválida. Por favor, digite 1, 2 ou 0.")

    except ValueError:
        print("Escolha inválida. Por favor, digite 1 ou 2.")
        


# ------------------------------------- área de testes -----------------------------------









# ------------------------------- área de rascunho -------------------------------

    # Caminho central do projeto
    #endereco_central = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/")


    # Caminho de saída para os arquivos gerados
    #endereco_saida = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/saida/")


# df_apontamento.to_excel(f"{path_saida}/apontamentos.xlsx", sheet_name="apontamentos", index=False)
# df_telemetria.to_excel(f"{path_saida}/telemetria.xlsx", sheet_name="telemetria", index=False)



# Arquivo do tipo excel
    #path_arquivo_alarmes = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/Alarmes - Regra de Negocio.xlsx")
    #path_arquivo_dicionario = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/Dicionario_Dados.xlsx")

    #path_arquivo_desenvolver_apontamentos = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/datasets/datasets/apontamentos/desenvolver_apontamentos.xlsx")
    #path_arquivo_dontgo = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/datasets/datasets/telemetria/desenvolver_dontgo.xlsx")


    # Dataframe das regras de negócio dos alarmes
    #df_alarm_CMA = pd.read_excel(f"{path_arquivo_alarmes}", sheet_name="CMA")
    #df_alarm_Tendencias = pd.read_excel(f"{path_arquivo_alarmes}", sheet_name="Tendências")
    #df_alarm_Eventos = pd.read_excel(f"{path_arquivo_alarmes}", sheet_name="Eventos O&M")

    # Dataframe do dicionário de dados
    #df_dicionario_apontamentos = pd.read_excel(f"{path_arquivo_dicionario}", sheet_name="Apontamentos")
    #df_dicionario_telemetria = pd.read_excel(f"{path_arquivo_dicionario}", sheet_name="Telemetria")

    # Dataframe do arquivo desenvolver_apontamentos.xlsx
    #df_desenvolver_apontamentos = pd.read_excel(f"{path_arquivo_desenvolver_apontamentos}")
    #df_desenvolver_dontgo = pd.read_excel(f"{path_arquivo_dontgo}")