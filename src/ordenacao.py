import os
import pandas as pd

# 1. Bubble Sort
def bubble_sort(lista):
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
                movimentacoes += 3
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

# 4. Shell Sort
def shell_sort(lista):
    arr = list(lista)
    n = len(arr)
    gap = n // 2
    comparacoes = 0
    movimentacoes = 0
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            movimentacoes += 1
            j = i
            while j >= gap:
                comparacoes += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    movimentacoes += 1
                    j -= gap
                else:
                    break
            arr[j] = temp
            movimentacoes += 1
        gap //= 2
    return arr, comparacoes, movimentacoes

# 5. Merge Sort
def merge(esquerda, direita):
    resultado = []
    i = j = 0
    comparacoes = 0
    movimentacoes = 0
    
    while i < len(esquerda) and j < len(direita):
        comparacoes += 1
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
        movimentacoes += 1
        
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
        movimentacoes += 1
        
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
        movimentacoes += 1
        
    return resultado, comparacoes, movimentacoes

def merge_sort_rec(arr):
    if len(arr) <= 1:
        return arr, 0, 0
    
    meio = len(arr) // 2
    esq, c_esq, m_esq = merge_sort_rec(arr[:meio])
    dir, c_dir, m_dir = merge_sort_rec(arr[meio:])
    
    combinado, c_merge, m_merge = merge(esq, dir)
    return combinado, c_esq + c_dir + c_merge, m_esq + m_dir + m_merge

def merge_sort(lista):
    arr = list(lista)
    return merge_sort_rec(arr)

# 6. Quick Sort
def quick_sort_rec(arr):
    if len(arr) <= 1:
        return arr, 0, 0
    
    pivo = arr[len(arr) // 2]
    menores = []
    iguais = []
    maiores = []
    comparacoes = 0
    movimentacoes = 0
    
    for x in arr:
        comparacoes += 1
        if x < pivo:
            menores.append(x)
            movimentacoes += 1
        elif x == pivo:
            iguais.append(x)
            movimentacoes += 1
        else:
            maiores.append(x)
            movimentacoes += 1
            
    ord_menores, c_menor, m_menor = quick_sort_rec(menores)
    ord_maiores, c_maior, m_maior = quick_sort_rec(maiores)
    
    resultado = ord_menores + iguais + ord_maiores
    return resultado, comparacoes + c_menor + c_maior, movimentacoes + m_menor + m_maior

def quick_sort(lista):
    arr = list(lista)
    return quick_sort_rec(arr)