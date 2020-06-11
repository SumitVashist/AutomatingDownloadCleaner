from zipfile import *
f=ZipFile("Files.zip","w",ZIP_DEFLATED)
f.write("dhiman.py")
f.write('bat.jpg')
f.write("new.py")
f.close()