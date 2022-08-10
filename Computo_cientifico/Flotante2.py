import numpy as np 


##número flotantes más grande de 64-bits (10 a  las 308)
import sys
a = sys.float_info.max
print(a)


b = 1e309
print(b)

pi = np.pi
print(pi)


print(np.finfo(float).eps)
# 2.22044604925e-16

print(np.finfo(np.float32).eps)
# 1.19209e-07


#truncamiento de números
#Operaciones: Suma y multiplicación
from math import trunc
k1 = 1e8 ##Este valor es la presición (el número de digitos después del cero)
trunc1 = trunc( ((5/7) + (1/3)) * k1 ) / k1 #Se trunca al valor respecto a la presición <k> seleccionada
print (trunc1)


k2 = 1e5
print(k2)
trunc2 = trunc( ((5/7) + (1/3)) * k2 ) / k2
print (trunc2)

error_absoluto = abs(trunc1-trunc2)
print(error_absoluto)
#Se observa que el erro absoluto para la suma es del orden de 10^-6

error_relativo = (abs(trunc1-trunc2)) / (abs(trunc1))
print(error_relativo)
#Se observa que el erro absoluto para la suma es del orden de 10^-6


