import xml.etree.ElementTree as ET
import re
import cgi
import shutil


print("Content-type: text/plain; charset=utf-8\n")




form = cgi.FieldStorage()



###########################
xml=str(form.getvalue("xml_value"))
xml2=str(form.getvalue("mk_value"))
y=xml2.replace("C:","").replace("\\","/")+"/"+xml
original = r''+str(y)
target = r'/Users/Romain/AppData/Local/Programs/Python/Python37/FileEncryptor/upload/'

shutil.move(original,target)


with open("tst.txt","w") as f:
	f.write(xml+'\n')
	f.write(xml2)
	f.close()

#######################################"
