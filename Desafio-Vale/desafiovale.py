from re import search

import pandas as pd
from pathlib import Path
import os

def __prepare():

    # Arquivos do tipo parquet    
    path_arquivo_apontamento = Path("datasets/datasets/apontamentos/")
    path_arquivo_telemetria_jan = Path(f"{path_arquivo_apontamento}/telemetry_jan.parquet")
    path_arquivo_telemetria_feb = Path(f"{path_arquivo_apontamento}/telemetry_feb.parquet")
    path_arquivo_telemetria_mar = Path(f"{path_arquivo_apontamento}/telemetry_mar.parquet")
    path_arquivo_telemetria_abr = Path(f"{path_arquivo_apontamento}/telemetry_abr.parquet")
    path_arquivo_telemetria_may = Path(f"{path_arquivo_apontamento}/telemetry_may.parquet")
    path_arquivo_telemetria_jun = Path(f"{path_arquivo_apontamento}/telemetry_jun.parquet")


    # Arquivo do tipo excel
    path_arquivo_alarmes = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/Alarmes - Regra de Negocio.xlsx")
    path_arquivo_dicionario = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/Dicionario_Dados.xlsx")

    path_arquivo_desenvolver_apontamentos = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/datasets/datasets/desenvolver_apontamentos.xlsx")
    path_arquivo_dontgo = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/datasets/datasets/telemetria/desenvolver_dontgo.xlsx")




    df_apontamento = pd.read_parquet(f"{path_arquivo_apontamento}//desenvolver_apontamentos.parquet").head(100)
    # df_telemetria = pd.read_parquet(f"{path_arquivo_telemetria}").head(20)


    # Dataframe das regras de negócio dos alarmes
    df_alarm_CMA = pd.read_excel(f"{path_arquivo_alarmes}", sheet_name="CMA")
    df_alarm_Tendencias = pd.read_excel(f"{path_arquivo_alarmes}", sheet_name="Tendências")
    df_alarm_Eventos = pd.read_excel(f"{path_arquivo_alarmes}", sheet_name="Eventos O&M")

    # Dataframe do dicionário de dados
    df_dicionario_apontamentos = pd.read_excel(f"{path_arquivo_dicionario}", sheet_name="Apontamentos")
    df_dicionario_telemetria = pd.read_excel(f"{path_arquivo_dicionario}", sheet_name="Telemetria")

    # Dataframe do arquivo desenvolver_apontamentos.xlsx
    df_desenvolver_apontamentos = pd.read_excel(f"{path_arquivo_desenvolver_apontamentos}")
    df_desenvolver_dontgo = pd.read_excel(f"{path_arquivo_dontgo}")



def __define_path():
    try: 
        chosen_path = input("Escolha o caminho do projeto (1 - Serviço, 2 - Casa, 0 - Sair): ")
        print('oi')
        while(chosen_path in {1,2,0}):
            print("inside while")
            match chosen_path:
                case 1:
                    path_central = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/")
                    path_saida = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/saida/")
                    print("1")
                    break
                case 2:
                    path_central = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/") # Editar
                    path_saida = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/saida/") # Editar
                    print("2")
                    break
                case 0:
                    print("Saindo do programa...")
                    print(0)
                    break
                case _:
                    print("Escolha inválida. Por favor, digite 1, 2 ou 0.")
    except ValueError:
        print("Escolha inválida. Por favor, digite 1 ou 2.")
        



    # Caminho central do projeto
    path_central = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/")


    # Caminho de saída para os arquivos gerados
    path_saida = Path("C:/Users/paulo.oliveira/Desktop/Python/Vale/saida/")

#print(df_apontamento[df_apontamento["Número do Protocolo:"] == "12345"])


#print(df_apontamento)

# print(df_telemetria)
#print(df_alarm_CMA[df_alarm_CMA["EVENTO"] == "*tire*"])

#print(df_alarm_CMA[df_alarm_CMA["EVENTO"].str.contains("Active", case=False, na=False)])

# print(os.path.isfile(f"{path_arquivo_apontamento}//desenvolver_apontamentos.parquet"))

# df_apontamento.to_excel(f"{path_saida}/apontamentos.xlsx", sheet_name="apontamentos", index=False)
# df_telemetria.to_excel(f"{path_saida}/telemetria.xlsx", sheet_name="telemetria", index=False)