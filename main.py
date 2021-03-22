import os
import json
import openpyxl
from models import Fixture, Menu, Book, Path

def main():
    path = Path()
    menu = Menu()
    menu.instructions()
    while True:
        # menu.de_entrada()
        try:
            excel_filename = input("Ingresa el nombre del archivo de excel: ")
            excel_exists = path.check_existence(excel_filename)
            if excel_exists:

                # File found notification for the user.
                menu.file_found()

                # Tras haber verificado que el archivo existe, se crea el path para cargar el libro con openpyxl.
                excel_file_path = path.book_path(excel_filename)
                
                # Book settings
                book = Book(excel_file_path)
                book_headers = book.get_headers()
                book_rows = book.get_list_of_rows()

                app_name = input("Ingresa el nombre del app de tu proyecto Django: ")
                model_name = input("Ingresa el nombre del modelo de tu app: ")

                fx = Fixture(
                    app=app_name,
                    model=model_name,
                    headers=book_headers,
                    list_of_fields=book_rows,
                )
                fx.create_objects()
                fx.create_json_file(path.json_dir)

                menu.task_completed()
                break
            else:
                menu.file_not_found()

        except ValueError:
            print("Ingresa el nombre del archivo.")
            print("")
            pass

if __name__ == '__main__':
    main()