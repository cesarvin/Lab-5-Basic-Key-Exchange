# Jorge Azmitia 15202
# Codigo basado en https://sublimerobots.com/2015/01/simple-diffie-hellman-example-python/
from __future__ import print_function

#Variables compartidas / Publicas
#Primo p
PrimoCompartido = int(input("Por favor ingrese un numero primo para hacer el modulo: "))
#Base para operacion b
Base = int(input("Por favor ingrese el numero que sera la base de la operacion "))

#Variables indiciduales/diferentes, privadas
#A
Secreto_Alicia = int(input("Por favor ingrese que numero sera el secreto de alicia: "))
#B
Secreto_Bob = int(input("Por favor ingrese que numero sera el secreto de bob: ") )
 
print( "Variables compartidas:")
print( "    Publicly Shared Prime: " , PrimoCompartido )
print( "    Publicly Shared Base:  " , Base )
 
# Alice Sends Bob A* = b^B mod p
A = (Base**Secreto_Alicia) % PrimoCompartido
print( "\n  Lo que envia Alicia: " , A )
 
# Bob Sends Alice B* = b^B mod p
B = (Base ** Secreto_Bob) % PrimoCompartido
print( "\n  Lo que envia Bob: ", B )
 
print( "\n\n" )
print( "Secreto comun calculado por:" )
# Alice Computes Shared Secret: s = B*^A mod p
secretocomunalicia = (B ** Secreto_Alicia) % PrimoCompartido
print( "    Alicia : ", secretocomunalicia )
 
# Bob Computes Shared Secret: s = A*^B mod p
secretocomunbob = (A**Secreto_Bob) % PrimoCompartido
print( "    Bob : ", secretocomunbob )
