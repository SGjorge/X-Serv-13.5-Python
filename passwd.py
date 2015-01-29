#!/usr/bin/python

# -*- coding: utf-8 -*-

fich = open("/etc/passwd","r")
lineas = fich.readlines()
dic = {}

for linea in lineas:
    conf = linea.split(":")
    username = conf[0]
    shell = conf [-1][: -1]
    dic[username] = shell

print dic
print "el numero de usuarios es: " + str(len(lineas))

print "root: " + dic["root"]
try:
	print "imaginario: " + dic["imaginario"]
except KeyError:
	print "palabra clave del diccionario incorrecta"
fich.close()
