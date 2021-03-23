# Django Fixture Maker (en español).

Este repo contiene el código para convertir un archivo de excel (con extensión .xlsx) en un archivo JSON, con el formato necesasrio para que el [command loaddata](https://docs.djangoproject.com/en/3.1/ref/django-admin/#django-admin-loaddata) de Django lo pueda interpretar correctamente.
Para más información sobre cómo funcionan las fixturas y los comandos para hacerlas efectivas en la base de datos referirse a la [documentación](https://docs.djangoproject.com/en/3.1/howto/initial-data/) oficial de Django.

### Puedes ver el video del walkthrough [aquí](https://youtu.be/KY-O_nJrlkw).

## Instrucciones:

* El repositorio cuenta con 2 directorios (excel y json). El directorio excel es donde deben vivir los archivos que quieres convertir a una fixtura JSON. Cuando el programa te pida ingresar el nombre del archivo de excel debes escribir sólo el nombre SIN la extensión (.xlsx). Este archivo debe estar dentro del directorio "excel", de otra manera el programa no podrá encontrar el archivo.
* Cuando se ejecute el programa, la fixtura creada será almacenada en la carpeta "json".
* 
* Debes crear un ambiente virtual, activarlo e instalar los requirements del proyecto:
```
pip install -r requirements.txt
```
* Seguidamente puedes iniciar el programa:
```
python main.py
```

### Disclaimers:
* El programa solo ha sido probado en Windows 10.
* El programa solo funciona (por el momento) con models.CharField() -> es decir, sólo renderiza strings. Leer el [release note](https://github.com/soloamilkar/django-fixtures-maker/releases/tag/v0.01) para más info.
