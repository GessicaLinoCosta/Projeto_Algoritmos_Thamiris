import os
import pandas as pd

# 1. Bubble Sort
def bubble_sort(lista):
    # Cria uma cópia para não alterar a lista original diretamente
    arr = list(lista)
    n = len(arr)
    comparacoes = 0
    movimentacoes = 0
    
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movimentacoes += 3  # Troca envolve 3 atribuições
                trocou = True
        if not trocou:
            break
    return arr, comparacoes, movimentacoes

# 2. Selection Sort
def selection_sort(lista):
    arr = list(lista)
    n = len(arr)
    comparacoes = 0
    movimentacoes = 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            movimentacoes += 3
    return arr, comparacoes, movimentacoes

# 3. Insertion Sort
def insertion_sort(lista):
    arr = list(lista)
    comparacoes = 0
    movimentacoes = 0
    
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                movimentacoes += 1
                j -= 1
            else:
                break
        arr[j + 1] = chave
        movimentacoes += 1
    return arr, comparacoes, movimentacoes

# --- Bloco de Teste ---
if __name__ == "__main__":
    caminho_csv = os.path.join("Dados", "base_1000_ordenada.csv.csv")
    
    if os.path.exists(caminho_csv):
        df = pd.read_csv(caminho_csv)
        # Vamos pegar numa amostra pequena (ex: os primeiros 50 IDs) para testar a ordenação rápida
        ids_amostra = df['id_cliente'].head(50).tolist()
        
        print(f"Amostra original (primeiros 10): {ids_amostra[:10]}...\n")
        
        # Testar Bubble Sort
        res_bubble, comp_b, mov_b = bubble_sort(ids_amostra)
        print(f"Bubble Sort -> Comparações: {comp_b} | Movimentações: {mov_b}")
        
        # Testar Selection Sort
        res_select, comp_s, mov_s = selection_sort(ids_amostra)
        print(f"Selection Sort -> Comparações: {comp_s} | Movimentações: {mov_s}")
        
        # Testar Insertion Sort
        res_insert, comp_i, mov_i = insertion_sort(ids_amostra)
        print(f"Insertion Sort -> Comparações: {comp_i} | Movimentações: {mov_i}")
    else:
        print("Ficheiro CSV não encontrado.")