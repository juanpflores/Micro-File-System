#!/usr/bin/python
# -*- coding: utf-8 -*-

# import modules used here.

# Import sysy as a standard library.
import sys
import os


# Gather our code in a main() function
def main():
	global band
	band = 0
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
			dispatcher[comando]()
	else:
		print("File not found.")



def unzip(file_zip):
	'''Unzips the main file'''
	if len(file_zip) > 0:
		os.system("unzip FILE_SYSTEM.zip")
		print("Se descomprimio el zip")
	else:
		print("No existe el zip")


def remove_file():
	'''Remove file to the system'''
	print("¿Qué archivo deseas borrar?")
	file = input()
	os.system("ls | grep "+ file +" > tmp")
	archivo = open("tmp", "r")
	find_file = archivo.readline()
	if len(find_file) > 0:
		os.system("rm -rf " + find_file)
		print("DONE!!!")
	else:
		print("FILE NOT FOUND")

def newdir():
	'''Add a new directory to the system'''
	print("¿Cómo se va a llamar la carpeta?")
	print("Maximo 6 caracteres.")
	user_input = input()
	path = os.getcwd()

	if len(user_input)<6:
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
	user_input = input()

	if len(user_input)<6:
		if not os.path.exists(user_input)
			f = open(user_input,'w')
			f.close()
		else:
			print("El archivo ya existe!")	
	else:
		print("Tu carpeta tiene más de 6 caracteres!")

def removedir():
	'''Delete a directory from the system'''
	print("¿Cómo se llamar la carpeta que quieres borrar?")
	user_input = input()

def edit():
	'''Edit file from the system'''
	print("¿Cómo se llama el archivo que quieres modificar? ")
	user_input = input()
	os.system("ls | grep "+ user_input +" > tmp")
	archivo = open("tmp", "r")
	find_file = archivo.readline()
	if len(find_file) > 0:
		os.system("vi " + find_file)
	else:
		print("FILE NOT FOUND")

def read():
	'''Reads the file from the system'''
	print("¿Cómo se llama el archivo que quieres leer?")
	user_input = input()

def goin():
	'''Go to the directory on the system'''
	print("¿Cómo se llama el directorio al que quieres entrar?")
	user_input = input()

def goback():
	'''Goes one directory back'''

def list_items():
	'''List the files on the directory from the system'''
	print("Archivos y Directorios existentes:")
	os.system("ls")

def exit():
	'''Closes the file system'''
	global band
	band = 1

def help():
	'''Print the commands available for the user with more context.'''

#We create a dispatcher dictionary for the bash functions. 
dispatcher = {'newdir': newdir, 'newfile': newfile, 'removedir':removedir, 'removefile':remove_file, 'edit':edit, 'goin':goin, 'goback':goback, 'list-items':list_items, 'help':help, 'read':read, 'exit': exit}

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()