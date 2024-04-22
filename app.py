from flask import Flask, request
from PROJETO02.defs import buscar_cidades, extrair_nomes, quick_sort, merge_sort, bubble_sort, selection_sort, insertion_sort
import time

# Instanciação da aplicação Flask
app = Flask(__name__)

# Rota para obter a lista completa de nomes de cidades do banco de dados
@app.route("/lista_cidades")
def todas_cidades():
    dados_cidades = buscar_cidades()  # Busca os dados completos das cidades
    nomes_cidades = extrair_nomes(dados_cidades)  # Extrai apenas os nomes das cidades
    return nomes_cidades

# Rota para ordenar nomes de cidades usando Quick Sort
@app.route("/ordenar_quick")
def ordenar_quick():
    tempo_inicial = time.time()  # Início da medição de tempo
    cidades = buscar_cidades()
    quick_sort(cidades)
    nomes_cidades = extrair_nomes(cidades)
    tempo_final = time.time()  # Fim da medição de tempo
    print(f"Tempo de execução de /ordenar_quick: {tempo_final - tempo_inicial} segundos")
    return nomes_cidades

# Rota para ordenar nomes de cidades usando Merge Sort
@app.route("/ordenar_merge")
def ordenar_merge():
    tempo_inicial = time.time()
    cidades = buscar_cidades()
    merge_sort(cidades)
    nomes_cidades = extrair_nomes(cidades)
    tempo_final = time.time()
    print(f"Tempo de execução de /ordenar_merge: {tempo_final - tempo_inicial} segundos")
    return nomes_cidades

# Rota para ordenar nomes de cidades usando Bubble Sort
@app.route("/ordenar_bubble")
def ordenar_bubble():
    tempo_inicial = time.time()
    cidades = buscar_cidades()
    bubble_sort(cidades)
    nomes_cidades = extrair_nomes(cidades)
    tempo_final = time.time()
    print(f"Tempo de execução de /ordenar_bubble: {tempo_final - tempo_inicial} segundos")
    return nomes_cidades

# Rota para ordenar nomes de cidades usando Selection Sort
@app.route("/ordenar_selection")
def ordenar_selection():
    tempo_inicial = time.time()
    cidades = buscar_cidades()
    selection_sort(cidades)
    nomes_cidades = extrair_nomes(cidades)
    tempo_final = time.time()
    print(f"Tempo de execução de /ordenar_selection: {tempo_final - tempo_inicial} segundos")
    return nomes_cidades

# Rota para ordenar nomes de cidades usando Insertion Sort
@app.route("/ordenar_insertion")
def ordenar_insertion():
    tempo_inicial = time.time()
    cidades = buscar_cidades()
    insertion_sort(cidades)
    nomes_cidades = extrair_nomes(cidades)
    tempo_final = time.time()
    print(f"Tempo de execução de /ordenar_insertion: {tempo_final - tempo_inicial} segundos")
    return nomes_cidades

if __name__ == "_main_":
    app.run(debug=True)