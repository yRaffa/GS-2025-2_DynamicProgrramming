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
