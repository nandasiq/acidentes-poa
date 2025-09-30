"""
Constantes do projeto (colunas, categorias, coordenadas, anos).
"""

# Colunas
COLS_CAT = ['regiao', 'tipo_acid', 'dia_sem', 'noite_dia']
COLS_STR = ['log1', 'log2']
COLS_INT = [
    'queda_arr', 'feridos', 'feridos_gr', 'fatais', 'ups',
    'auto', 'taxi', 'lotacao', 'onibus_urb', 'onibus_met',
    'onibus_int', 'caminhao', 'moto', 'carroca', 'bicicleta',
    'outro', 'cont_vit', 'patinete', 'idacidente', 'predial1'
]
COLS_VEICULOS = [
    'auto', 'bicicleta', 'lotacao', 'onibus_urb',
    'onibus_met', 'onibus_int', 'caminhao',
    'moto', 'carroca', 'taxi', 'outro', 'patinete'
]

# Open-Meteo
URL = "https://archive-api.open-meteo.com/v1/archive"
COORD = {
    "NORTE":  (-29.987, -51.165),
    "LESTE":  (-30.040, -51.160),
    "CENTRO": (-30.027, -51.220),
    "SUL":    (-30.120, -51.230)
}
ANOS = [2020, 2021, 2022, 2023, 2024, 2025]
