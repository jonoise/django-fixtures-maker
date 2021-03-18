import os
import json
import openpyxl
from fixture import Fixture
from utils import (
    check_existence,
    check_extension,
    total_col_xlsx,
    get_headers_xlsx,
)

# inputs
filename = input("Nombre del archivo: ")
extension = input("Extensión del archivo (csv or xlsx) : ")
# paths
file_path = os.getcwd() + f'\\{filename}.{extension}'
results_path = os.getcwd() + f'\\{"results"}'


