import os
import pandas as pd

# 1. Busca Linear Iterativa
def busca_linear_iterativa(lista, alvo):
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            return i, comparacoes
    return -1, comparacoes

# 2. Busca Linear Recursiva
def busca_linear_recursiva_aux(lista, alvo, indice, comparacoes):
    if indice >= len(lista):
        return -1, comparacoes
    comparacoes += 1
    if lista[indice] == alvo:
        return indice, comparacoes
    return busca_linear_recursiva_aux(lista, alvo, indice + 1, comparacoes)

def busca_linear_recursiva(lista, alvo):
    return busca_linear_recursiva_aux(lista, alvo, 0, 0)

# 3. Busca Binária Iterativa (exige lista ordenada)
def busca_binaria_iterativa(lista, alvo):
    comparacoes = 0
    esquerda = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        if lista[meio] == alvo:
            return meio, comparacoes
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1, comparacoes

# 4. Busca Binária Recursiva (exige lista ordenada)
def busca_binaria_recursiva_aux(lista, alvo, esquerda, direita, comparacoes):
    if esquerda > direita:
        return -1, comparacoes
    
    meio = (esquerda + direita) // 2
    comparacoes += 1
    
    if lista[meio] == alvo:
        return meio, comparacoes
    elif lista[meio] < alvo:
        return busca_binaria_recursiva_aux(lista, alvo, meio + 1, direita, comparacoes)
    else:
        return busca_binaria_recursiva_aux(lista, alvo, esquerda, meio - 1, comparacoes)

def busca_binaria_recursiva(lista, alvo):
    return busca_binaria_recursiva_aux(lista, alvo, 0, len(lista) - 1, 0)

# --- Bloco de Teste Principal ---
if __name__ == "__main__":
    caminho_csv = os.path.join("Dados", "base_1000_ordenada.csv.csv")
    
    if os.path.exists(caminho_csv):
        df = pd.read_csv(caminho_csv)
        ids = df['id_cliente'].tolist()
        
        # Vamos testar procurando o ID que está a meio da base
        alvo_teste = ids[len(ids) // 2]
        print(f"A procurar pelo ID de cliente: {alvo_teste}\n")
        
        # Testar Busca Linear Iterativa
        pos, comp = busca_linear_iterativa(ids, alvo_teste)
        print(f"Busca Linear Iterativa -> Índice: {pos} | Comparações: {comp}")
        
        # Testar Busca Linear Recursiva
        pos, comp = busca_linear_recursiva(ids, alvo_teste)
        print(f"Busca Linear Recursiva -> Índice: {pos} | Comparações: {comp}")
        
        # Testar Busca Binária Iterativa
        pos, comp = busca_binaria_iterativa(ids, alvo_teste)
        print(f"Busca Binária Iterativa -> Índice: {pos} | Comparações: {comp}")
        
        # Testar Busca Binária Recursiva
        pos, comp = busca_binaria_recursiva(ids, alvo_teste)
        print(f"Busca Binária Recursiva -> Índice: {pos} | Comparações: {comp}")
    else:
        print(f"Erro: O ficheiro não foi encontrado em {caminho_csv}")
