#Practicas desarrolladas en Python3.6


##Instalación de Python3.6:

    Para instalar la versión 3.6 de Python necesitaremos descargarnos el instalador desde la propia página:

    [Web oficial de Python](https://www.python.org/downloads/release/python-360/)

##Asegurando el funcionamiento:
    para asegurarnos de que las aplicaciones hechas con arcade funcionen, debermos hacer un downgrade de pip hasta la versión 9.0.1:

    pip install --force-reinstall pip==9.0.1

##Instalación de los paquetes necesarios para ejecutar las practicas. Nos situamos en la carpeta con el archivo requirements.txt y ejecutamos el comando:

    pip install -r requirements.txt

Este comando habrá realizado todas las configuraciones necesarias para poder ejecutar las prácticas correctamente, por lo que solo queda ejecutar las practicas con:

    python3 "nombre_practica".py