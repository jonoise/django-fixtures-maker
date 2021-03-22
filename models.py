import os
import json
import openpyxl

class Fixture():
    def __init__(self, app, model, headers=None, list_of_fields=None):
        self.app = app
        self.model = model
        self.headers = headers
        self.fields = list_of_fields
        self.objects = []
        self.object_ = {}
        self.body = {}

    def create_objects(self):
        """Esta función crea los objetos y les da el formato adecuado para que puedan ser interpretados
        por el LoadData de Django. Por cada objeto crea un pk y un body. El 'body' son los fields.
        Tras completar este proceso por cada item en cada columna por cada row del archivo de excel
        lo añade a la lista de objetos."""
        pk = 0
        for row in self.fields:
            pk += 1
            self.object_ = {}
            self.body = {}
            self.object_['model'] = '{}.{}'.format(self.app, self.model).lower()
            self.object_['pk'] = pk
            for index, value in enumerate(row):
                self.body[self.headers[index]] = value
            self.object_['fields'] = self.body
            self.objects.append(self.object_)

    def return_objects(self):
        """Retorna los objetos en formato Python. Una lista de diccionarios."""
        return self.objects
        
    def return_json(self):
        """Retorna los objetos en formato Json. Una lista de objectos Json."""
        return json.dumps(self.objects, indent=2)
    
    def create_json_file(self, json_dir):
        """Se crea la fixtura.json con el nombrel del app (según las conveciones de Django)"""
        with open(f'{json_dir}\\{self.app}.json', 'w') as f:
            f.write(self.return_json())


class Path():
    def __init__(self):
        self.pwd = os.getcwd() # Obtiene el pwd.
        self.extension = 'xlsx' # La única extensión disponible
        self.excel_dir = f'{self.pwd}\\excel' # Input path para los excels
        self.json_dir = f'{self.pwd}\\json' # Output path para las Fixtures

    def check_existence(self, filename):
        """Revisa si el "filename" está en el directorio de excel."""
        current_dir = os.listdir(self.excel_dir)
        if f'{filename}.{self.extension}' in current_dir:
            return True
        else:
            return False

    def book_path(self, filename):
        """Retorna el path para ser ingresado en la clase 'Book'."""
        return f'{self.excel_dir}\\{filename}.{self.extension}'

class Book():
    def __init__(self, book_object):
        self.book = openpyxl.load_workbook(book_object) 
    
    def get_number_cols(self):
        """Retorna el número de columnas"""
        columns = self.book.active.columns
        total_columns = 0
        for column in columns:
            total_columns += 1
        return total_columns

    def get_number_rows(self):
        """Retorna el número de rows"""
        rows = self.book.active.rows
        total_rows = 0
        for row in rows:
            total_rows +=1
        return total_rows - 1

    def get_headers(self):
        """Retorna los headers del archivo de excel"""
        headers_list = []
        for i in range(self.get_number_cols()):
            headers_list.append(self.book.active.cell(row=1, column=i+1).value)
        return headers_list

    def get_list_of_rows(self):
        """Retorna un 2D array donde el segundo nivel son los valores de cada columna por row"""
        rows = self.book.active.rows
        rows_ = []
        for row in rows:
            row_appended = []
            for value in row:
                row_appended.append(value.value)
            rows_.append(row_appended)
        rows_.pop(0)
        return rows_

class Menu():
    def de_entrada(self):
        print('Menú principal. Selecciona un número:')
        print('1- Seleccionar el archivo de excel.')
        print('2- Crear Fixtura')
        print('9- Salir')
        print('')

    def instructions(self):
        print('')
        print('Para leer la documentación detallada ejecuta el comando "help". O ve al repositorio del proyecto')
        print('y lee el README.md.')
        print('')
        print('Instrucciones:')
        print('El programa busca en la carpeta "excel" por tus archivos de excel en formato XLSX. Si tu archivo')
        print('de excel tiene otra extensión, debes cambiar el formato del archivo y posteriormente agregarlo a')
        print('carpeta "excel". Cuando se te solicite el nombre del archivo, escribe SOLO el nombre (sin la extensión).')
        print('')

    def file_found(self):
        print('')
        print('Archivo encontrado')
        print('')

    def file_not_found(self):
        print('')
        print('No se encontró el archivo, asegúrate de que escribiste bien el nombre y no estás')
        print('agregando la extensión del archivo. Asegúrate que tu archivo vive en la carpeta "excel".') 
        print('Escribe sólo el nombre. Inténtalo de nuevo.')
        print('')

    def task_completed(self):
        print('')
        print('Tu fixtura ha sido creada satisfactoriamente. Revisa la carpeta "json".')
        print('')
        