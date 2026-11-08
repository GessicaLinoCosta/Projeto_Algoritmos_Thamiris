import os
import pandas as pd

# Caminho para a base de dados que temos no projeto
caminho_csv = os.path.join("Dados", "base_1000_ordenada.csv.csv")

print(f"A procurar o arquivo em: {caminho_csv}")

# Verifica se o ficheiro existe antes de tentar ler
if os.path.exists(caminho_csv):
    # Lê o arquivo CSV usando a biblioteca pandas
    df = pd.read_csv(caminho_csv)
    
    print("\n--- Informações Gerais da Base de Dados ---")
    print(df.info())
    
    print("\n--- Primeiras 5 linhas do arquivo ---")
    print(df.head())
else:
    print(f"Erro: O arquivo não foi encontrado no caminho especificado: {caminho_csv}")
    