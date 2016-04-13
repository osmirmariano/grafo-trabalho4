import matplotlib.pyplot as plt
import networkx as nx

arquivo = open('matriz.txt', 'r')
linha = arquivo.readline()
v=0
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
   for m in range(0,6): #vai de 0 a 5
       for n in range(0,6):
           if m != n:
               arestas.append((m,n))        
arq.close()
print "\n"
print "Arestas: ",arestas
print "\n"