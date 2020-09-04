# encoding: utf-8
import os, sys
import generateCertificate
import pandas as pd

#python certificateManager.py 'Base de inscritos Edu Webinar 3- 24 de Julio - Leon Thahtemberg.xlsx' 'Nombres y apellidos (como quieres que se escriba en tu constancia)' 

if len(sys.argv) == 3:
    file_name   = sys.argv[1]
    column_name = sys.argv[2]
else:
    print 'failure: incorrect parameters'
    sys.exit(2)

name = "Student Name"

dateFile = open("date.txt","r")
date = dateFile.read()

textFile = open("text.txt","r")
text = textFile.read()

df = pd.read_excel(file_name)

for ind in df.index:
    # name of column with names
    name = df[column_name][ind].encode("utf-8").strip()
    generateCertificate.generateCertificate(name,date,text)