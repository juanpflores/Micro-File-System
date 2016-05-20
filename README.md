# Micro-File System Morgan


## Installation

Descargar el proyecto en el directorio deseado.
* SSH
```sh
git clone git@github.com:juanpflores94/Micro-File-System.git
```
* HTTPS
```sh
git clone https://github.com/juanpflores94/Micro-File-System.git
```

## Usage

Se necesitan de las siguientes características para correr el sistema.

* Sistema Operativo GNU/Linux
* Python 3.x
* Bash
* zip para GNU/Linux

El sistema de inicio tiene un archivo llamado 'FILE_SYSTEM.zip' que simula el entorno donde el sistema de archivos trabajará. Importante no borrarlo.
Iniciar el sistema desde bash con con el comando ```python3 main.py```. 
Se debe introducir un comando valido seguido de un ```ENTER```. A continuación se pedirá la información correspondiente al comando (Algunos comandos no requieren de información adicional).

##Commands

1. newdir: Crea un nuevo directorio dentro del directorio actual. (Maximo 6 caracteres)
2. newfile: Crea un nuevo archivo dentro del directorio actual. (Maximo 6 caracteres)
3. removedir: Borra un directorio. (Debe existir)
4. removefile: Borra un archivo. (Debe existir)
5. edit: Edita un archivo. (Utiliza el programa 'vi'. Debe existir el archivo)
6. goin: Permite entrar a un directorio. (Debe existir)
7. goback: Permite salir del directorio actual posicionando en el directorio anterior. (En caso de estar en raíz no hará nada)
8. list-items: Despliega los directorios y archivos existentes.
9. read: Despliega el contenido de un archivo. (Debe existir)
11. help: Despliega detalles de los comandos existentes.
12. exit: Salida del Sistema de Archivos Morgan.
 
## Notes

Ignorar el archivo 'tmp' en los directorios. Existe exclusivamente para el correcto funcionamiento del sistema.
