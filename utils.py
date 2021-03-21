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
    if extension == 'xlsx':
        print('Seleccionaste XLSX, asegurate que tu archivo sigue las siguientes pautas:')
        print('')
        print('1- Los títulos de columnas tienen el mismo nombre que los fields que tus modelos en la base de datos.')
        print('2- Recuerda que los fields que estén mapeados a un Foreign Key deben incluir el número entero del ID del modelo padre.')

    else:
        print('Por el momento sólo aceptamos archivos con extensiones CSV o XLSX. Puedes editar el archivo desde tu administrador de hojas de cálculo favorito')
        print('y cambiar la extensión del archivo a una conocida por el programa. (CSV o XLSX). Recuerda que si eliges CSV, el delimitante deben ser comas (,) y no puntos y coma (;)')


###########################################
# Gives the number of columns in the file #
###########################################
def get_number_cols(book):
    columns = book.active.columns
    total_columns = 0
    for column in columns:
        total_columns += 1
    return total_columns


###########################################
## Gives the number of rows in the file ###
###########################################
def get_number_rows(book):
    rows = book.active.rows
    total_rows = 0
    for row in rows:
        total_rows +=1
    return total_rows - 1 


########################################
# Return a list of titles on first col #
########################################
def get_headers(book):
    headers_list = []
    for i in range(get_number_cols(book)):
        headers_list.append(book.active.cell(row=1, column=i+1).value)
    return headers_list


#########################################
# Return each row value for each column #
#########################################
def rows_generator(book):
    for i in range(get_number_rows(book)):
        for j in range(get_number_cols(book)):
            yield book.active.cell(row=i+1, column=j+1).value

def get_list_of_rows(book):
    rows = book.active.rows
    rows_ = []
    for row in rows:
        row_appended = []
        for value in row:
            row_appended.append(value.value)
        rows_.append(row_appended)
    rows_.pop(0)
    return rows_