bits_16 = list(range(0,15))
#print(bits_16)
resultado= 0
for i in bits_16:
    resultado_i = 2**i
    resultado = resultado + resultado_i
    print(resultado)


