#!/usr/bin/env python
#-*-coding: utf-8-*-
import matplotlib.pyplot as plt
import networkx as nx
from numpy import matrix 

f = open('matriz.txt') 
a = f.read() # a variavel "a" guarda o conteudo do arquivo 
f.close() 

file_obj = file("matriz.txt", "rU") 

data = [] 
data_append = data.append 
for line in file_obj: 
        data_append([int(x) for x in line.split() if x]) 
data = matrix(data)
print data

matriz = [ map(int, line.split()) for line in file('matriz.txt') if line.strip() ] 
print matriz
print matriz[1][1]

mat = matrix([ map(int, line.split()) for line in file('matriz.txt') if line.strip() ]) 
print mat

arquivo = open('matriz.txt', 'r')
linha = arquivo.readline()
v=0
cont=0
while linha:
   print linha,
   linha = arquivo.readline()
   v=v+1
arquivo.close()
print "\n\nVertices:",v,"\n"

arq = open('matriz.txt', 'r')
li = arq.readline()
arestas = []
while li:
   print li,
   li = arq.readline()
   for m in range(1,v+1): #vai de 1 a qtd de vertices
       for n in range(1,v+1):
           a=m
           if m != n:
               if cont != v:
                   cont=cont+1
                   arestas.append((m,n))                    
               
arq.close()
print "\n\nv:",v
print "cont:",cont
print "\n"
print "Arestas: ",arestas
print "\n"
