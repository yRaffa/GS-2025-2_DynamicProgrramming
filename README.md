# **🌐 FIAP GLOBAL SOLUTION 2025 - 2º SEMESTRE**

# 🐍 Dynamic Programming

## 👥 Integrantes (2ESPH)

```
RM 556197 | Caio Felipe de Lima Bezerra
RM 555490 | Marcos Vinícius da Silva Costa
RM 554736 | Rafael Federici de Oliveira
```

## 📕 Sobre o Projeto

### 📋 Relatório de Motor de Orientação de Habilidades (MOH)

Projeto desenvolvido para a disciplina Dynamic Programming, integrando Programação Dinâmica, Heurísticas, Simulação Monte Carlo, Análise Combinatória e Algoritmos Clássicos para orientar um Motor de Orientação de Habilidades (MOH).

## 📂 Estrutura do Projeto

``` bash
GS-2025-2_DynamicProgramming/
/data                        
  └── dados.py          # Conjunto de dados de entrada
/desafios                   
  ├── d1/               # Algoritmos para o Desafio 01
  ├── d2/               # Algoritmos para o Desafio 02
  ├── d3/               # Algoritmos para o Desafio 03
  ├── d4/               # Algoritmos para o Desafio 04
  └── d5/               # Algoritmos para o Desafio 05
/utils                      
  └── decorators.py     # Decorators para medição de tempo e momoria
  └── grafos.py         # Construção e Validação da etrutura de grafos
relatorio.ipynb         # Relatório Jupyter Notebook com análises e gráficos
README.md               # Documentação do projeto
```

## 🧠 Resumo dos Desafios

### 1️⃣ Desafio 1: Caminho de Valor Máximo

Modelo de DP multidimensional (Tempo e Complexidade) para encontrar o melhor caminho até S6.
Inclui simulação Monte Carlo com 1000 cenários e comparação determinístico × simulado.

### 2️⃣ Desafio 2: Verificação Crítica

Enumeração das 120 permutações das habilidades críticas (S3, S5, S7, S8, S9).
Validação do grafo (ciclos, nós órfãos), cálculo de custos e análise estatística.

### 3️⃣ Desafio 3: Pivô Mais Rápido

Heurística greedy (V/T) x solução ótima exaustiva.
Contraexemplo mostrando falha do método greedy.

### 4️⃣ Desafio 4: Trilhas Paralelas

Quick Sort implementado manualmente para ordenar as 12 habilidades originais.
Divisão em Sprint A e B + benchmark com sort nativo.

### 5️⃣ Desafio 5: Recomendar Próximas Habilidades

DP em horizonte finito (5 anos) para planejar trilha personalizada de aprendizado.
Probabilidades de mercado, score V×P, trilha recomendada, heatmap e gráficos de evolução.

## 🎲 Estrutura dos Dados

Os dados são armazenados no dicionário ``` dic_skills ```, onde cada chave representa um ID, e os valores são as linhas e colunas.

``` python
dic_skills = {
    'S1' : {'Nome': 'Programacao Basica (Python)',      'Tempo': 80,    'Valor': 3,     'Complexidade': 4,  'PreRequisito': [],              'UsoPrincipal': 'Base'},
    'S2' : {'Nome': 'Modelagem de Dados (SQL)',         'Tempo': 60,    'Valor': 4,     'Complexidade': 3,  'PreRequisito': [],              'UsoPrincipal': 'Base'},
    'S3' : {'Nome': 'Algoritmos Avancados',             'Tempo': 100,   'Valor': 7,     'Complexidade': 8,  'PreRequisito': ['S1'],          'UsoPrincipal': 'Critica (HC1)'},
    'S4' : {'Nome': 'Fundamentos de Machine Learning',  'Tempo': 120,   'Valor': 8,     'Complexidade': 9,  'PreRequisito': ['S1', 'S3'],    'UsoPrincipal': 'Nao Critica'},
    'S5' : {'Nome': 'Visualizacao de Dados (BI)',       'Tempo': 40,    'Valor': 6,     'Complexidade': 5,  'PreRequisito': ['S2'],          'UsoPrincipal': 'Critica (HC2)'},
    'S6' : {'Nome': 'IA Generativa Etica',              'Tempo': 150,   'Valor': 10,    'Complexidade': 10, 'PreRequisito': ['S4'],          'UsoPrincipal': 'Objetivo Final'},
    'S7' : {'Nome': 'Estruturas em Nuvem (AWS/Azure)',  'Tempo': 70,    'Valor': 5,     'Complexidade': 7,  'PreRequisito': [],              'UsoPrincipal': 'Critica (HC3)'},
    'S8' : {'Nome': 'APIs e Microsservicos',            'Tempo': 90,    'Valor': 6,     'Complexidade': 6,  'PreRequisito': ['S1'],          'UsoPrincipal': 'Critica (HC4)'},
    'S9' : {'Nome': 'DevOps &  CI/CD',                  'Tempo': 110,   'Valor': 9,     'Complexidade': 8,  'PreRequisito': ['S7', 'S8'],    'UsoPrincipal': 'Critica (HC5)'},
    'H10': {'Nome': 'Seguranca de Dados',               'Tempo': 60,    'Valor': 5,     'Complexidade': 6,  'PreRequisito': [],              'UsoPrincipal': 'Lista Grande'},
    'H11': {'Nome': 'Analise de Big Data',              'Tempo': 90,    'Valor': 8,     'Complexidade': 8,  'PreRequisito': ['S4'],          'UsoPrincipal': 'Lista Grande'},
    'H12': {'Nome': 'Introducao a IoT',                 'Tempo': 30,    'Valor': 3,     'Complexidade': 3,  'PreRequisito': [],              'UsoPrincipal': 'Lista Grande'}
}
```

## 🛠️ Tecnologias e Técnicas Utilizadas

- Python 3.10+
- NumPy
- Matplotlib / Seaborn
- pandas
- itertools
- Programação Dinâmica
- Quick Sort implementado manualmente
- Simulação Monte Carlo

## ▶️ Como Executar

#### **Clone o repositório:**

``` bash
git clone <repo_url>
cd SPRINT3_DynamicProgramming
```

#### **Instale as dependências:**

``` bash
pip install -r requirements.txt
```

#### **Para visualizar relatório:**

``` bash
jupyter notebook relatorio.ipynb
```

## 📄 Relatório Final

O arquivo ``` relatorio.ipynb ``` contém:

- Explicações técnicas
- Análises de complexidade
- Diagramas de estrutura de dados
- Evidências experimentais
- Conclusões por desafio
- Conclusão Geral