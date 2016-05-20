#!/usr/bin/python
# -*- coding: utf-8 -*-

# import modules used here.

# Import sysy as a standard library.
import sys
import os, shutil


# Gather our code in a main() function
def main():
	global band, in_dir
	band = 0
	in_dir = 0
	print('Hello Diego!')
	os.system("clear")
	os.system("ls | grep FILE_SYSTEM.zip > tmp")
	archivo = open("tmp", "r")
	find_zip = archivo.readline()
	if find_zip == "FILE_SYSTEM.zip\n":
		print("La carpeta existe")
		unzip(find_zip)
		os.chdir("FILE_SYSTEM")
		os.system("clear")
		print("========================================Micro System Morgan========================================")
		print("Lista de Comandos: newdir, newfile, removedir, removefile, edit, read, goin, goback, list-items, exit, help")
		while band != 1:		
			#The program reads the input and searchs it on the dispatcher.
			comando = input("user@machine$ ")
			if comando_valido(comando):
				dispatcher[comando]()
			else:
				print("¡Comando invalido!")
				print("Teclea 'help' para conocer los comandos disponibles")
		os.system("rm -rf tmp")
		os.chdir("..")
		os.system("zip -r FILE_SYSTEM.zip FILE_SYSTEM")
		os.system("rm -rf FILE_SYSTEM")
		os.system("clear")
		print("Saliendo...")
		print(""" ____________________________
< Developed by Ptolomeo Team >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||""")
	else:
		print("File not found.")


def unzip(file_zip):
	'''Unzips the main file'''
	if len(file_zip) > 0:
		os.system("unzip FILE_SYSTEM.zip")
		print("Se descomprimio el zip")
	else:
		print("No existe el zip")

def comando_valido(comando):
	if comando == "newdir" or comando == "newfile" or comando == "removefile" or comando == "removedir" or comando == "edit" or comando == "read" or comando == "goin" or comando == "goback" or comando == "list-items" or comando == "exit" or comando == "help":
		return True
	else:
		return False

def newdir():
	'''Add a new directory to the system'''
	print("¿Cómo se va a llamar la carpeta?")
	print("Maximo 6 caracteres.")
	user_input = input(">> ")
	path = os.getcwd()

	if len(user_input) < 6:
		if not os.path.exists(user_input):
			os.makedirs(user_input)
		else:
			print("La carpeta ya existe!")
	else:
		print("Tu carpeta tiene más de 6 caracteres!")

def newfile():
	'''Add a new File to the system'''
	print("¿Cómo se va a llamar archivo?")
	print("Maximo 6 caracteres.")
	user_input = input(">> ")

	if len(user_input) < 6:
		if not os.path.exists(user_input):
			f = open(user_input,'w')
			f.close()
		else:
			print("El archivo ya existe!")	
	else:
		print("Tu archivo tiene más de 6 caracteres!")

def removedir():
	'''Delete a directory from the system'''
	print("¿Cómo se llamar la carpeta que quieres borrar?")
	user_input = input(">> ")
	path = os.getcwd()

	if os.path.isdir(path+'/'+user_input):
		shutil.rmtree(user_input)

	else:
		print("El directorio no existe!")
		pass


def remove_file():
	'''Remove file to the system'''
	print("¿Qué archivo deseas borrar?")
	file = input(">> ")
	os.system("ls | grep "+ file +" > tmp")
	archivo = open("tmp", "r")
	find_file = archivo.readline()
	if len(find_file) > 0:
		os.system("rm -rf " + find_file)
	else:
		print("¡El archivo no existe!")

def edit():
	'''Edit file from the system'''
	print("¿Cómo se llama el archivo que quieres modificar? ")
	user_input = input(">> ")
	os.system("ls | grep "+ user_input +" > tmp")
	archivo = open("tmp", "r")
	find_file = archivo.readline()
	if len(find_file) > 0:
		os.system("vi " + find_file)
	else:
		print("¡El archivo no existe!")

def read():
	'''Reads the file from the system'''
	print("¿Cómo se llama el archivo que quieres leer?")
	user_input = input(">> ")
	if len(user_input) < 6:
		if os.path.exists(user_input):
			print("El Archivo '"+user_input+"' contiene: ")
			print("====================================")
			os.system("cat " + user_input)
			print("====================================")
		else:
			print("¡El archivo no existe!")	
	else:
		print("Tu achivo tiene más de 6 caracteres!")

def goin():
	'''Go to the directory on the system'''
	global in_dir
	print("¿Cómo se llama el directorio al que quieres entrar? ")
	user_input = input(">> ")
	os.system("ls | grep "+ user_input +" > tmp")
	archivo = open("tmp", "r")
	find_file = archivo.readline()
	if len(find_file) > 0:
		os.chdir(find_file[:-1])
		in_dir += 1
	else:
		print("¡El directorio no existe!")

def goback():
	'''Goes one directory back'''
	global in_dir
	if in_dir > 0:
		os.chdir("..")
		in_dir -= 1
	else:
		print("Imposible, estas en raíz [/]")

def list_items():
	'''List the files on the directory from the system'''
	os.system("ls --color=always")

def exit():
	'''Closes the file system'''
	global band
	
	band = 1

def help():
	'''Print the commands available for the user with more context.'''
	print("*******************************************************************************************************************************")
	print("[Command + ENTER]")
	print("1. newdir: Crea un nuevo directorio dentro del directorio actual. (Maximo 6 caracteres)")
	print("2. newfile: Crea un nuevo archivo dentro del directorio actual. (Maximo 6 caracteres)")
	print("3. removedir: Borra un directorio. (Debe existir)")
	print("4. removefile: Borra un archivo. (Debe existir)")
	print("5. edit: Edita un archivo. (Utiliza el programa 'vi'. Debe existir el archivo)")
	print("6. goin: Permite entrar a un directorio. (Debe existir)")
	print("7. goback: Permite salir del directorio actual posicionando en el directorio anterior. (En caso de estar en raíz no hará nada)")
	print("8. list-items: Despliega los directorios y archivos existentes.")
	print("9. read: Despliega el contenido de un archivo. (Debe existir)")
	print("11. help: Despliega detalles de los comandos existentes.")
	print("12. exit: Salida del Sistema de Archivos Morgan")
	print("*******************************************************************************************************************************")

#We create a dispatcher dictionary for the bash functions. 
dispatcher = {'newdir': newdir, 'newfile': newfile, 'removedir':removedir, 'removefile':remove_file, 'edit':edit, 'goin':goin, 'goback':goback, 'list-items':list_items, 'help':help, 'read':read, 'exit': exit}

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
