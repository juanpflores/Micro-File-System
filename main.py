#!/usr/bin/python

# import modules used here.

# Import sysy as a standard library.
import sys
import os
# Gather our code in a main() function
def main():
	print('Hello Diego!'), sys.argv[1]
	os.system("clear")
	os.system("ls | grep FILE_SYSTEM.zip > test")
	archivo = open("test", "r")
	find_zip = archivo.readline()
	if find_zip == "FILE_SYSTEM.zip\n":
		print("La carpeta existe")
		print("====Micro System Morgan====")
		unzip(find_zip)
		print("Lista de Comandos: newdir <name>, newfile <name>, removedir <name>, removefile <name>, edit <file>, goin <name>, goback, list, help")
		os.chdir("FILE_SYSTEM")
		os.system("pwd")
		comando = input()
	else:
		print("NOT FOUND =(")
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored

def unzip(file_zip):

	if len(file_zip) > 0:
		os.system("unzip FILE_SYSTEM.zip")
		print("Se descomprimio el zip")
		os.system("ls")
	else:
		print("No existe el zip")


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()