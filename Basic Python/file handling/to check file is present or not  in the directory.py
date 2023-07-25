from os.path import *
def main():
	filename = input("Enter file name with extension and directory: ")
	if not (isfile(filename)):
		print('Error, check input file name or check file name in directory')
		return
	print('file is present')
	file = open(filename, "r")
	file.close
main()
