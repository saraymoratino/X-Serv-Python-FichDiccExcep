#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero = open ("/etc/passwd", "r")
lineas = fichero.readlines()
diccionario = {}

for line in lineas:
	trocear = line.split(':')
	login = trocear [0]
	shell = trocear [-1][:-1]
	diccionario[login] = shell 
	
	
print diccionario['root']
try:
	print diccionario['imaginario']
except KeyError:
	print 'Not found'
	
