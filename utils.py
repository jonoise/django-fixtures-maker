import os
import openpyxl
import json

def check_existence(file_path):
    path_list = file_path.split('\\')
    file = path_list.pop()
    current_dir = os.listdir()
    if file in current_dir:
        return True
    else:
        return False

def check_extension(extension):
    if extension == 'csv':
        print('Seleccionaste CSV, asegurate que tu archivo sigue las siguientes pautas:')
        print('')
        print('1- Asegúrate que las casillas están separadas por comas (,) y no por punto y coma (;).')
        print('2- Si tu archivo cuenta con números, asegúrate que los decimales están separados por un punto (.) y no una coma (,).')
        print('3- Recuerda que los fields que estén mapeados a un Foreign Key deben incluir el número entero del ID del modelo padre.')
    
    if extension == 'xlsx':
        print('Seleccionaste XLSX, asegurate que tu archivo sigue las siguientes pautas:')
        print('')
        print('1- Los títulos de columnas tienen el mismo nombre que tus modelos en la base de datos.')
        print('2- Recuerda que los fields que estén mapeados a un Foreign Key deben incluir el número entero del ID del modelo padre.')

    else:
        print('Por el momento sólo aceptamos archivos con extensiones CSV o XLSX. Puedes editar el archivo desde tu administrador de hojas de cálculo favorito')
        print('y cambiar la extensión del archivo a una conocida por el programa. (CSV o XLSX). Recuerda que si eliges CSV, el delimitante deben ser comas (,) y no puntos y coma (;)')

def check_headers_csv(file):
    pass

def total_col_xlsx(book):
    columns = book.active.columns
    total_columns = 0
    for column in columns:
        total_columns += 1
    return total_columns

def get_headers_xlsx(book):
    headers = []
    for i in range(total_col(book)):
        headers.append(book0.cell(row=1, column=i+1).value)
    return headers