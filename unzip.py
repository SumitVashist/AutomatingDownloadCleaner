from zipfile import *
f=ZipFile("Files.zip","r",ZIP_STORED)
names=f.namelist()
for name in names:
	print("File Name : ",name)
	if name !='bat.jpg':
		print("The contents of file are:")
		f1=open(name,'r')
		print(f1.read())
		print()


import os
print(os.listdir("."))