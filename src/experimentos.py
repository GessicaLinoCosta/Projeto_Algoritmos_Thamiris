import os
import time
import statistics
import pandas as pd
from ordenacao import bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort, quick_sort

def executar_experimento(algoritmo_func, lista_dados, repeticoes=30):
    tempos = []
    comparacoes_lista = []
    movimentacoes_lista = []
    
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        _, comp, mov = algoritmo_func(lista_dados)
        fim = time.perf_counter()
        
        tempos.append((fim - inicio) * 1000) # Milissegundos
        comparacoes_lista.append(comp)
        movimentacoes_lista.append(mov)
        
    return {
        "tempo_medio": statistics.mean(tempos),
        "tempo_mediano": statistics.median(tempos),
        "tempo_desvio": statistics.stdev(tempos) if len(tempos) > 1 else 0,
        "comp_media": statistics.mean(comparacoes_lista),
        "mov_media": statistics.mean(movimentacoes_lista)
    }

if __name__ == "__main__":
    # Dicionário com os nomes exatos dos ficheiros atuais na pasta Dados
    bases = {
        1000: "base_1000_ordenada.csv.csv",
        10000: "base_10000.csv.csv",
        100000: "base_100000.csv.csv"
    }
    
    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Shell Sort", shell_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    os.makedirs("Resultados", exist_ok=True)
    
    for tamanho, nome_ficheiro in bases.items():
        caminho_csv = os.path.join("Dados", nome_ficheiro)
        
        if os.path.exists(caminho_csv):
            print(f"\n--- A processar base de {tamanho} registos ({nome_ficheiro}) ---")
            df = pd.read_csv(caminho_csv, sep=None, engine='python')
            
            # Selecionar automaticamente a coluna de dados
            coluna_dados = 'id_cliente' if 'id_cliente' in df.columns else df.columns[0]
            dados = df[coluna_dados].tolist()
            
            resultados = []
            for nome_alg, func in algoritmos:
                print(f"  -> A testar {nome_alg}...")
                res = executar_experimento(func, dados, repeticoes=30)
                
                resultados.append({
                    "Algoritmo": nome_alg,
                    "Tamanho_Base": tamanho,
                    "Tempo_Medio_ms": res["tempo_medio"],
                    "Tempo_Mediano_ms": res["tempo_mediano"],
                    "Desvio_Padrao": res["tempo_desvio"],
                    "Comparacoes_Medias": res["comp_media"],
                    "Movimentacoes_Medias": res["mov_media"]
                })
            
            # Guardar resultado individual para cada tamanho de base
            df_res = pd.DataFrame(resultados)
            caminho_saida = os.path.join("Resultados", f"resumo_experimentos_{tamanho}.csv")
            df_res.to_csv(caminho_saida, index=False)
            print(f"  [OK] Resultados guardados em {caminho_saida}")
        else:
            print(f"\nAviso: Ficheiro '{nome_ficheiro}' não encontrado na pasta 'Dados/'.")
